"""
main.py — CLI entry point for Plant Care AI Detection System.

Commands:
  diagnose      Run diagnosis on a local leaf image
  train         Train / fine-tune model using transfer learning
  serve         Start Flask web server
  history       Display recent diagnoses
  export-csv    Export diagnosis history to CSV
  init-db       Initialize SQLite database schema
  download-data Download PlantVillage dataset
"""

import argparse
import csv
import json
import sys
from pathlib import Path

# Force UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

import config
from utils.logger import get_logger

logger = get_logger("plant_care_cli")


def cmd_init_db(args):
    """Initialize database tables and seed demo data."""
    from database.db import init_db
    init_db()
    print("✅ Database initialized successfully.")


def cmd_diagnose(args):
    """Diagnose an image file."""
    from core.classifier import diagnose_image

    img_path = Path(args.image)
    if not img_path.exists():
        print(f"❌ Error: Image file '{args.image}' not found.")
        sys.exit(1)

    print(f"🔬 Analyzing image: {img_path} …")
    try:
        res = diagnose_image(img_path, top_k=args.top)
    except Exception as exc:
        print(f"❌ Diagnosis failed: {exc}")
        sys.exit(1)

    print("\n" + "=" * 60)
    print(f"🌿 DIAGNOSIS RESULT: {res['top_prediction']}")
    print(f"🎯 Confidence:     {res['top_confidence_pct']}%")
    print(f"💚 Health Score:   {res['health_score']}/100")
    print(f"⚠️ Severity:       {res['severity']}")
    if res['uncertain']:
        print("⚠️ Warning: Result confidence below threshold — needs review.")
    print("=" * 60)

    print("\n📊 Top Predictions:")
    for i, p in enumerate(res['predictions'], 1):
        print(f"  {i}. {p['label']:<40} {p['confidence']*100:6.2f}%")

    print("\n💊 Recommendations Summary:")
    recs = res['recommendations'].get('recommendations', [])
    for r in recs[:5]:
        print(f"  - [{r['category']}] {r['text']}")
    print("=" * 60 + "\n")


def cmd_train(args):
    """Train or fine-tune model."""
    from core.trainer import train
    dataset_path = Path(args.data_dir) if args.data_dir else config.DATASET_DIR

    print(f"🚀 Starting model training on dataset at: {dataset_path}")
    print(f"   Epochs: Phase 1 = {args.epochs}, Batch Size = {args.batch_size}")
    if args.subset < 1.0:
        print(f"   Subset fraction: {args.subset * 100}%")

    train(
        dataset_dir=dataset_path,
        epochs_phase1=args.epochs,
        epochs_phase2=args.epochs_phase2 or (args.epochs * 2),
        batch_size=args.batch_size,
        subset_fraction=args.subset,
    )
    print("✅ Training complete.")


def cmd_serve(args):
    """Start web server."""
    from app import create_app
    app = create_app()
    port = args.port or config.SERVER_PORT
    host = args.host or config.SERVER_HOST
    print(f"🌐 Starting web server on http://{host}:{port} …")
    app.run(host=host, port=port, debug=args.debug)


def cmd_history(args):
    """List recent diagnosis history."""
    from database.repository import list_diagnoses
    res = list_diagnoses(page=1, per_page=args.limit)
    items = res['items']

    if not items:
        print("No diagnosis history found.")
        return

    print(f"\n📜 Recent Diagnoses (Total: {res['total']}):")
    print("-" * 80)
    print(f"{'ID':<4} {'Date':<11} {'Health':<8} {'Severity':<8} {'Top Prediction':<35}")
    print("-" * 80)
    for row in items:
        date_str = str(row.get('created_at', ''))[:10]
        print(
            f"{row['id']:<4} {date_str:<11} {row['health_score']:<8} "
            f"{row['severity']:<8} {row['top_prediction'][:34]:<35}"
        )
    print("-" * 80 + "\n")


def cmd_export_csv(args):
    """Export history to CSV file."""
    from database.repository import export_all_to_list
    rows = export_all_to_list()
    out_path = Path(args.out)

    if not rows:
        print("No history to export.")
        return

    fieldnames = [
        "id", "image_name", "image_path", "top_prediction",
        "top_confidence", "health_score", "severity", "created_at"
    ]

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Exported {len(rows)} records to '{out_path}'.")


def cmd_download_data(args):
    """Download PlantVillage dataset script caller."""
    from scripts.download_dataset import download_plant_village
    download_plant_village(auto_download=args.auto_download)


def build_parser() -> argparse.ArgumentParser:
    """Construct CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="plant_care",
        description="Plant Care AI Detection System — Command Line Interface",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init-db
    p_init = subparsers.add_parser("init-db", help="Initialize SQLite database schema")
    p_init.set_defaults(func=cmd_init_db)

    # diagnose
    p_diag = subparsers.add_parser("diagnose", help="Diagnose a plant leaf image")
    p_diag.add_argument("--image", "-i", required=True, help="Path to leaf image file")
    p_diag.add_argument("--top", "-t", type=int, default=5, help="Number of predictions")
    p_diag.set_defaults(func=cmd_diagnose)

    # train
    p_train = subparsers.add_parser("train", help="Train AI classification model")
    p_train.add_argument("--epochs", type=int, default=5, help="Phase 1 epochs")
    p_train.add_argument("--epochs-phase2", type=int, default=None, help="Phase 2 fine-tune epochs")
    p_train.add_argument("--batch-size", type=int, default=32, help="Training batch size")
    p_train.add_argument("--subset", type=float, default=1.0, help="Subset fraction of data (e.g. 0.2)")
    p_train.add_argument("--data-dir", help="Path to raw PlantVillage dataset directory")
    p_train.set_defaults(func=cmd_train)

    # serve
    p_serve = subparsers.add_parser("serve", help="Start Flask REST API & Web Dashboard")
    p_serve.add_argument("--port", "-p", type=int, help="Port to listen on")
    p_serve.add_argument("--host", help="Host to bind to")
    p_serve.add_argument("--debug", action="store_true", help="Enable Flask debug mode")
    p_serve.set_defaults(func=cmd_serve)

    # history
    p_hist = subparsers.add_parser("history", help="List recent diagnoses")
    p_hist.add_argument("--limit", type=int, default=20, help="Number of records to show")
    p_hist.set_defaults(func=cmd_history)

    # export-csv
    p_exp = subparsers.add_parser("export-csv", help="Export history to CSV file")
    p_exp.add_argument("--out", "-o", default="diagnoses.csv", help="Output CSV path")
    p_exp.set_defaults(func=cmd_export_csv)

    # download-data
    p_dl = subparsers.add_parser("download-data", help="Download PlantVillage dataset")
    p_dl.add_argument("--auto-download", action="store_true", help="Attempt automatic download via kagglehub")
    p_dl.set_defaults(func=cmd_download_data)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == "__main__":
    main()
