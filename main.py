from src.data_generator import generate_synthetic_data
from src.expense_analyzer import ExpenseAnalyzer
import os

def main():
    print(">> Starting Personal Expense Tracker Execution...\n")
    
    # Define paths
    data_path = "data/synthetic_expenses.csv"
    
    # Step 1: Generate Synthetic Data
    print("--- Phase 1: Data Generation ---")
    generate_synthetic_data(output_path=data_path, num_records=300)
    print("\n")
    
    # Step 2: Initialize Analyzer
    print("--- Phase 2: Data Loading & Cleaning ---")
    analyzer = ExpenseAnalyzer(data_path=data_path)
    if not analyzer.load_and_clean_data():
        print("Execution failed during data loading.")
        return
    print("\n")
    
    # Step 3: Analyze and Visualize
    print("--- Phase 3: Data Analysis & Visualization ---")
    analyzer.generate_category_analysis()
    analyzer.generate_monthly_trend()
    analyzer.generate_payment_method_analysis()
    analyzer.generate_daily_trend()
    print("\n")
    
    # Step 4: Final Report
    analyzer.print_financial_insights()
    
    print("[SUCCESS] Project Execution Completed Successfully!")
    print("Check the 'images/' folder for visualizations and 'outputs/' for CSV reports.")

if __name__ == "__main__":
    main()
