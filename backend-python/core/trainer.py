"""
core/trainer.py — Transfer learning training script using MobileNetV2.

Implements two-phase training:
  Phase 1: Freeze base, train new head (5 epochs)
  Phase 2: Unfreeze top 20 layers, fine-tune (10 epochs, lower LR)
"""

import json
import os
import sys
from pathlib import Path
from typing import Optional, Tuple

from utils.logger import get_logger
import config

logger = get_logger(__name__)


def build_model(num_classes: int) -> "tf.keras.Model":
    """
    Build a MobileNetV2-based transfer learning model.

    Args:
        num_classes: Number of output classes.

    Returns:
        Compiled Keras model (base layers frozen).
    """
    import tensorflow as tf
    from tensorflow.keras import layers, Model
    from tensorflow.keras.applications import MobileNetV2

    base_model = MobileNetV2(
        input_shape=(config.IMAGE_SIZE, config.IMAGE_SIZE, 3),
        include_top=False,
        weights="imagenet",
    )
    base_model.trainable = False  # Freeze for Phase 1

    inputs = tf.keras.Input(shape=(config.IMAGE_SIZE, config.IMAGE_SIZE, 3))
    x = base_model(inputs, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dropout(0.3)(x)
    x = layers.Dense(256, activation="relu")(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, activation="softmax")(x)

    model = Model(inputs, outputs, name="plant_care_mobilenetv2")
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=config.LEARNING_RATE),
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )
    logger.info(
        "Built model: %d parameters, %d trainable",
        model.count_params(),
        sum(tf.size(v).numpy() for v in model.trainable_variables),
    )
    return model, base_model


def create_data_generators(
    dataset_dir: Path,
    image_size: int,
    batch_size: int,
    subset_fraction: float = 1.0,
) -> Tuple:
    """
    Create ImageDataGenerators with augmentation for train/val/test.

    Args:
        dataset_dir: Root directory containing per-class subdirectories.
        image_size: Target image size.
        batch_size: Mini-batch size.
        subset_fraction: Fraction of data to use (0.0–1.0). Useful for fast training.

    Returns:
        (train_gen, val_gen, test_gen, class_names) tuple.
    """
    import tensorflow as tf
    from tensorflow.keras.preprocessing.image import ImageDataGenerator
    import numpy as np

    # Augmentation for training
    train_datagen = ImageDataGenerator(
        rescale=1.0 / 255.0,
        rotation_range=20,
        zoom_range=0.2,
        horizontal_flip=True,
        brightness_range=[0.8, 1.2],
        shear_range=0.2,
        fill_mode="nearest",
        validation_split=0.2,  # 80% train, 20% val from training data
    )

    # No augmentation for val/test — only rescale
    test_datagen = ImageDataGenerator(rescale=1.0 / 255.0)

    train_gen = train_datagen.flow_from_directory(
        str(dataset_dir),
        target_size=(image_size, image_size),
        batch_size=batch_size,
        class_mode="categorical",
        subset="training",
        shuffle=True,
        seed=42,
    )

    val_gen = train_datagen.flow_from_directory(
        str(dataset_dir),
        target_size=(image_size, image_size),
        batch_size=batch_size,
        class_mode="categorical",
        subset="validation",
        shuffle=False,
        seed=42,
    )

    # For test set: use the same directory (full set without augment)
    test_gen = test_datagen.flow_from_directory(
        str(dataset_dir),
        target_size=(image_size, image_size),
        batch_size=batch_size,
        class_mode="categorical",
        shuffle=False,
    )

    # Apply subset
    if subset_fraction < 1.0:
        n_train = max(1, int(train_gen.samples * subset_fraction))
        n_val = max(1, int(val_gen.samples * subset_fraction))
        train_gen.samples = n_train
        train_gen._set_index_array()
        val_gen.samples = n_val
        val_gen._set_index_array()
        logger.info(
            "Subset mode: using %.0f%% of data (%d train, %d val samples)",
            subset_fraction * 100,
            n_train,
            n_val,
        )

    class_names = list(train_gen.class_indices.keys())
    return train_gen, val_gen, test_gen, class_names


def train(
    dataset_dir: Optional[Path] = None,
    epochs_phase1: int = None,
    epochs_phase2: int = None,
    batch_size: int = None,
    subset_fraction: float = 1.0,
    output_dir: Optional[Path] = None,
) -> None:
    """
    Run full two-phase transfer learning training.

    Args:
        dataset_dir: Path to PlantVillage dataset root.
        epochs_phase1: Epochs for frozen-base phase.
        epochs_phase2: Epochs for fine-tuning phase.
        batch_size: Batch size for training.
        subset_fraction: Fraction of dataset to use (0.0–1.0).
        output_dir: Directory to save model and labels.
    """
    import tensorflow as tf
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from sklearn.metrics import classification_report, confusion_matrix
    import numpy as np

    dataset_dir = dataset_dir or config.DATASET_DIR
    epochs_phase1 = epochs_phase1 or config.TRAIN_EPOCHS_PHASE1
    epochs_phase2 = epochs_phase2 or config.TRAIN_EPOCHS_PHASE2
    batch_size = batch_size or config.BATCH_SIZE
    output_dir = output_dir or config.MODELS_DIR

    if not dataset_dir.exists() or not any(dataset_dir.iterdir()):
        logger.error(
            "Dataset not found at '%s'.\n"
            "Please download PlantVillage from Kaggle:\n"
            "  https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset\n"
            "Extract to: %s\n"
            "Or run: python main.py download-data --auto-download",
            dataset_dir,
            dataset_dir,
        )
        sys.exit(1)

    logger.info("Creating data generators from '%s' …", dataset_dir)
    train_gen, val_gen, test_gen, class_names = create_data_generators(
        dataset_dir, config.IMAGE_SIZE, batch_size, subset_fraction
    )
    num_classes = len(class_names)
    logger.info("Found %d classes: %s", num_classes, class_names[:5])

    # Save labels.json
    output_dir.mkdir(parents=True, exist_ok=True)
    labels_path = output_dir / "labels.json"
    with open(labels_path, "w", encoding="utf-8") as f:
        json.dump(class_names, f, indent=2, ensure_ascii=False)
    logger.info("Saved labels to '%s'.", labels_path)

    # Build model
    model, base_model = build_model(num_classes)
    model_path = output_dir / "plant_model.h5"

    # ── Phase 1: Train new head ───────────────────────────────────────────────
    logger.info("=== Phase 1: Training head (%d epochs) ===", epochs_phase1)
    callbacks_p1 = [
        tf.keras.callbacks.EarlyStopping(
            monitor="val_loss", patience=3, restore_best_weights=True
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor="val_loss", factor=0.5, patience=2, min_lr=1e-7, verbose=1
        ),
        tf.keras.callbacks.ModelCheckpoint(
            str(model_path), monitor="val_accuracy", save_best_only=True, verbose=1
        ),
    ]
    history_p1 = model.fit(
        train_gen,
        validation_data=val_gen,
        epochs=epochs_phase1,
        callbacks=callbacks_p1,
    )

    # ── Phase 2: Fine-tune top layers ─────────────────────────────────────────
    logger.info("=== Phase 2: Fine-tuning top 20 layers (%d epochs) ===", epochs_phase2)
    base_model.trainable = True
    for layer in base_model.layers[:-20]:
        layer.trainable = False

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=config.FINE_TUNE_LR),
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )
    callbacks_p2 = [
        tf.keras.callbacks.EarlyStopping(
            monitor="val_loss", patience=5, restore_best_weights=True
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor="val_loss", factor=0.3, patience=3, min_lr=1e-8, verbose=1
        ),
        tf.keras.callbacks.ModelCheckpoint(
            str(model_path), monitor="val_accuracy", save_best_only=True, verbose=1
        ),
    ]
    history_p2 = model.fit(
        train_gen,
        validation_data=val_gen,
        epochs=epochs_phase2,
        callbacks=callbacks_p2,
    )

    logger.info("Training complete. Best model saved to '%s'.", model_path)

    # ── Training Curves ───────────────────────────────────────────────────────
    _save_training_curves(history_p1, history_p2, output_dir)

    # ── Evaluation ────────────────────────────────────────────────────────────
    logger.info("Evaluating model on test set …")
    test_gen.reset()
    y_pred_probs = model.predict(test_gen, verbose=1)
    y_pred = np.argmax(y_pred_probs, axis=1)
    y_true = test_gen.classes[:len(y_pred)]

    report = classification_report(y_true, y_pred, target_names=class_names, zero_division=0)
    logger.info("Classification Report:\n%s", report)

    _save_confusion_matrix(y_true, y_pred, class_names, output_dir)
    logger.info("All outputs saved to '%s'.", output_dir)


def _save_training_curves(history_p1, history_p2, output_dir: Path) -> None:
    """Save combined training curves from both phases."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    acc_p1 = history_p1.history.get("accuracy", [])
    val_acc_p1 = history_p1.history.get("val_accuracy", [])
    loss_p1 = history_p1.history.get("loss", [])
    val_loss_p1 = history_p1.history.get("val_loss", [])

    acc_p2 = history_p2.history.get("accuracy", [])
    val_acc_p2 = history_p2.history.get("val_accuracy", [])
    loss_p2 = history_p2.history.get("loss", [])
    val_loss_p2 = history_p2.history.get("val_loss", [])

    acc = acc_p1 + acc_p2
    val_acc = val_acc_p1 + val_acc_p2
    loss = loss_p1 + loss_p2
    val_loss = val_loss_p1 + val_loss_p2
    epochs = range(1, len(acc) + 1)
    split = len(acc_p1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("Plant Care AI — Training Curves", fontsize=14)

    ax1.plot(epochs, acc, "b-o", markersize=4, label="Train Accuracy")
    ax1.plot(epochs, val_acc, "r-o", markersize=4, label="Val Accuracy")
    ax1.axvline(x=split, color="gray", linestyle="--", alpha=0.7, label="Fine-tune start")
    ax1.set_xlabel("Epoch")
    ax1.set_ylabel("Accuracy")
    ax1.set_title("Accuracy")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(epochs, loss, "b-o", markersize=4, label="Train Loss")
    ax2.plot(epochs, val_loss, "r-o", markersize=4, label="Val Loss")
    ax2.axvline(x=split, color="gray", linestyle="--", alpha=0.7, label="Fine-tune start")
    ax2.set_xlabel("Epoch")
    ax2.set_ylabel("Loss")
    ax2.set_title("Loss")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    curve_path = output_dir / "training_curves.png"
    plt.savefig(str(curve_path), dpi=120, bbox_inches="tight")
    plt.close(fig)
    logger.info("Training curves saved to '%s'.", curve_path)


def _save_confusion_matrix(y_true, y_pred, class_names, output_dir: Path) -> None:
    """Save a confusion matrix plot."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn.metrics import confusion_matrix

    cm = confusion_matrix(y_true, y_pred)
    cm_norm = cm.astype("float") / (cm.sum(axis=1, keepdims=True) + 1e-8)

    n = len(class_names)
    fig_size = max(10, n * 0.6)
    fig, ax = plt.subplots(figsize=(fig_size, fig_size))
    im = ax.imshow(cm_norm, interpolation="nearest", cmap=plt.cm.Blues)
    plt.colorbar(im, ax=ax)
    ax.set(
        xticks=np.arange(n),
        yticks=np.arange(n),
        xticklabels=class_names,
        yticklabels=class_names,
        xlabel="Predicted label",
        ylabel="True label",
        title="Normalized Confusion Matrix",
    )
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", fontsize=7)
    plt.setp(ax.get_yticklabels(), fontsize=7)
    plt.tight_layout()
    cm_path = output_dir / "confusion_matrix.png"
    plt.savefig(str(cm_path), dpi=120, bbox_inches="tight")
    plt.close(fig)
    logger.info("Confusion matrix saved to '%s'.", cm_path)
