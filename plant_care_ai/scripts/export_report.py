"""
scripts/export_report.py — Export diagnosis analytics and CSV summary.
"""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from database.repository import export_all_to_list, get_stats
import pandas as pd


def export_report(output_csv: str = "diagnosis_report.csv"):
    """Export diagnosis data to CSV and display summary stats."""
    stats = get_stats()
    print("\n📊 DIAGNOSIS DATABASE ANALYTICS SUMMARY")
    print("=" * 50)
    print(f"Total Diagnoses Recorded: {stats['total']}")
    print(f"Healthy Plants Count:     {stats['healthy_count']}")
    print(f"Diseased Plants Count:    {stats['diseased_count']}")
    print(f"Overall Health Rate:      {stats['healthy_pct']}%")
    print(f"Most Prevalent Disease:   {stats['top_disease']}")
    print("=" * 50)

    rows = export_all_to_list()
    if not rows:
        print("No diagnosis records available to export.")
        return

    df = pd.DataFrame(rows)
    df.to_csv(output_csv, index=False)
    print(f"✅ Full report exported successfully to '{output_csv}'.\n")


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "diagnosis_report.csv"
    export_report(out)
