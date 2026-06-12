"""
main.py
-------
Entry point for the EDA project.
Run:  python main.py
"""

import sys
import os

# Make src/ importable when running from the project root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from data_loader       import load_and_save
from statistics_summary import print_report
from visualizations    import generate_all_charts
from report_generator  import generate_report
import statistics_summary as stats_module


def main():
    print("\n" + "=" * 60)
    print("  EDA PROJECT — Iris Flower Dataset")
    print("=" * 60)

    # 1. Load data
    print("\n[1/4] Loading dataset ...")
    df = load_and_save("data/iris.csv")

    # 2. Print statistics to terminal
    print("\n[2/4] Computing statistics ...")
    print_report(df)

    # 3. Generate all charts
    print("\n[3/4] Generating charts ...")
    chart_paths = generate_all_charts(df)

    # 4. Build PDF report
    print("\n[4/4] Building PDF report ...")
    generate_report(df, chart_paths, stats_module, "report/EDA_Report.pdf")

    print("\n" + "=" * 60)
    print("  ALL DONE!")
    print("  data/iris.csv          — raw dataset")
    print("  charts/                — 7 PNG visualisations")
    print("  report/EDA_Report.pdf  — submission-ready PDF")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
