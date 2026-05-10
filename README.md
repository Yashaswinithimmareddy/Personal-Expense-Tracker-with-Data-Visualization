# Personal Expense Tracker with Data Visualization 📊

## 🌟 Project Overview
The **Personal Expense Tracker** is a Python-based end-to-end data analysis project that simulates real-world personal finance management. It automatically generates synthetic expense data, cleans and processes it using Pandas, and creates comprehensive visual insights using Matplotlib and Seaborn. This project serves as a robust proof-of-work for Data Analysts, Python Developers, and Business Analysts.

## ❓ Problem Statement
Tracking daily expenses manually is tedious, prone to errors, and rarely provides actionable insights. Individuals and small businesses often struggle to identify where their money goes, making budgeting and financial planning difficult. 

This project solves that by transforming raw transaction data into visual, easy-to-understand reports that highlight spending habits, monthly trends, and primary payment methods.

## 💼 Industry Relevance
- **Finance/FinTech**: Demonstrates handling of transactional data, currency formatting, and aggregations.
- **Data Analytics**: Showcases data cleaning, grouping, time-series analysis, and visualization.
- **Automation**: Automates the pipeline from raw CSV data to final exported charts and summary reports.

## ✨ Features
- **Automated Data Generation**: Simulates realistic daily expenses with categories, amounts, and dates.
- **Data Cleaning Pipeline**: Handles missing values, enforces data types, and parses dates.
- **Category-Wise Analysis**: Identifies the highest spending categories.
- **Monthly Trend Tracking**: Maps out spending behavior over time to spot seasonal spikes.
- **Payment Method Breakdown**: Visualizes the preferred modes of transaction.
- **Automated Reporting**: Generates summary CSVs and high-quality PNG charts automatically.

## 🛠 Tech Stack
- **Language**: Python 3.x
- **Data Manipulation**: Pandas, NumPy
- **Data Visualization**: Matplotlib, Seaborn
- **File Handling**: OS, CSV

## 📂 Folder Structure
```text
Personal-Expense-Tracker-Visualization/
│
├── data/                  # Contains raw/synthetic expense data
├── src/                   # Core Python modules
│   ├── data_generator.py  # Script to simulate expenses
│   ├── expense_analyzer.py# Core data processing & visualization logic
├── outputs/               # Generated summary reports (CSVs)
├── images/                # Generated visualizations (PNGs)
├── docs/                  # Detailed project documentation and interview prep
├── notebooks/             # For future Jupyter Notebooks
├── main.py                # Main orchestrator script
├── requirements.txt       # Project dependencies
└── README.md              # Project overview (this file)
```

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Personal-Expense-Tracker-Visualization.git
   cd Personal-Expense-Tracker-Visualization
   ```

2. **Set up virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Project**:
   ```bash
   python main.py
   ```

## 📈 Sample Output
```text
========================================
📊 FINANCIAL INSIGHTS REPORT
========================================
💰 Total Spending: $42,530.50
📈 Highest Spending Category: Food & Dining ($12,450.00)
📅 Average Daily Spending: $236.28
========================================
```

## 🖼 Screenshots
*(After running the project, upload your generated charts from the `images/` folder here)*
- `images/category_bar_chart.png`
- `images/monthly_trend_line.png`
- `images/payment_method_pie.png`
- `images/daily_trend.png`

## 🎓 Learning Outcomes
- **ETL Processes**: Extracting data from CSV, transforming it (cleaning/grouping), and loading results.
- **Pandas Mastery**: Proficiency in `.groupby()`, `.dt.to_period()`, `.sum()`, and handling datetimes.
- **Visualization**: Creating compelling, industry-standard visualizations using Seaborn color palettes.
- **Software Engineering**: Building modular code, using OOP principles, and separating concerns.
