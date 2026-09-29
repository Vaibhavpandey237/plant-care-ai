"""
scripts/create_demo_leaves.py — Generates synthetic leaf images for offline demonstration.
"""

import math
from pathlib import Path
from PIL import Image, ImageDraw

DEMO_DIR = Path(__file__).resolve().parent.parent / "demo"
DEMO_DIR.mkdir(parents=True, exist_ok=True)


def draw_leaf(width=400, height=400, leaf_color=(34, 139, 34), spot_color=None) -> Image.Image:
    """Draw a synthetic leaf shape with optional disease spots."""
    img = Image.new("RGB", (width, height), color=(240, 240, 240))
    draw = ImageDraw.Draw(img)

    # Draw leaf body (ellipse / polygon shape)
    leaf_shape = [
        (width // 2, 40),            # tip
        (width - 60, height // 3),   # right shoulder
        (width - 80, 2 * height // 3), # right base
        (width // 2, height - 60),   # stem junction
        (80, 2 * height // 3),       # left base
        (60, height // 3),           # left shoulder
    ]
    draw.polygon(leaf_shape, fill=leaf_color, outline=(0, 100, 0))

    # Draw center vein
    draw.line([(width // 2, 40), (width // 2, height - 40)], fill=(0, 80, 0), width=4)

    # Draw side veins
    for y in range(80, height - 80, 40):
        draw.line([(width // 2, y), (width // 2 + 80, y - 20)], fill=(0, 90, 0), width=2)
        draw.line([(width // 2, y), (width // 2 - 80, y - 20)], fill=(0, 90, 0), width=2)

    # Draw stem
    draw.line([(width // 2, height - 60), (width // 2, height - 10)], fill=(101, 67, 33), width=8)

    # Draw disease spots if specified
    if spot_color:
        spots = [
            (160, 140, 25),
            (240, 200, 35),
            (180, 260, 20),
            (220, 110, 18),
            (130, 220, 30),
        ]
        for cx, cy, r in spots:
            draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=spot_color, outline=(50, 20, 0))

    return img


def generate_demo_files():
    # 1. Healthy green leaf
    leaf1 = draw_leaf(leaf_color=(46, 139, 87))
    leaf1.save(DEMO_DIR / "leaf1.png")
    print(f"Created {DEMO_DIR / 'leaf1.png'}")

    # 2. Diseased leaf with brown spots (Scab / Blight)
    leaf2 = draw_leaf(leaf_color=(107, 142, 35), spot_color=(101, 67, 33))
    leaf2.save(DEMO_DIR / "leaf2.png")
    print(f"Created {DEMO_DIR / 'leaf2.png'}")

    # 3. Diseased leaf with dark spots
    leaf3 = draw_leaf(leaf_color=(128, 128, 0), spot_color=(40, 20, 10))
    leaf3.save(DEMO_DIR / "leaf3.png")
    print(f"Created {DEMO_DIR / 'leaf3.png'}")


if __name__ == "__main__":
    generate_demo_files()
