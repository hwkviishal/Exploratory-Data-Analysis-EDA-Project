# Exploratory Data Analysis — Iris Flower Dataset

A complete Python EDA project built for a Data Science Internship submission.

## Project Structure

```
eda-project/
├── main.py                  # Entry point — run this
├── requirements.txt         # Python dependencies
├── README.md
├── data/
│   └── iris.csv             # Auto-generated on first run
├── charts/                  # Auto-generated PNG charts
│   ├── 01_distributions.png
│   ├── 02_boxplots.png
│   ├── 03_pairplot.png
│   ├── 04_correlation_heatmap.png
│   ├── 05_violins.png
│   ├── 06_key_scatter_petal.png
│   └── 07_mean_comparison.png
├── report/
│   └── EDA_Report.pdf       # Final submission PDF
└── src/
    ├── data_loader.py        # Dataset loading & saving
    ├── statistics_summary.py # Descriptive stats, ANOVA, correlation
    ├── visualizations.py     # All matplotlib/seaborn charts
    └── report_generator.py   # ReportLab PDF builder
```

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

This will:
1. Download and save the Iris dataset to `data/iris.csv`
2. Print statistical summaries to the terminal
3. Generate 7 charts in `charts/`
4. Build a submission-ready PDF at `report/EDA_Report.pdf`

## Key Findings

- **Petal dimensions** are the strongest inter-species discriminators (ANOVA F > 1000)
- **Setosa** is fully linearly separable from the other two species
- **Petal length ↔ petal width** correlation: r = 0.96 (near-perfect collinearity)
- **Sepal width** is the weakest predictor (r ≈ –0.12 with species)
- Recommended classifiers: Logistic Regression, LDA, k-NN, SVM-RBF

## Dataset

UCI ML Repository — Iris Flower Dataset  
Fisher, R. A. (1936). *The use of multiple measurements in taxonomic problems.*
