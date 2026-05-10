import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class ExpenseAnalyzer:
    def __init__(self, data_path="data/synthetic_expenses.csv"):
        self.data_path = data_path
        self.df = None
        
        # Output directories
        self.images_dir = "images"
        self.reports_dir = "outputs"
        
        os.makedirs(self.images_dir, exist_ok=True)
        os.makedirs(self.reports_dir, exist_ok=True)

    def load_and_clean_data(self):
        """Loads expense data and performs basic cleaning."""
        try:
            self.df = pd.read_csv(self.data_path)
            # Convert 'Date' to datetime object
            self.df['Date'] = pd.to_datetime(self.df['Date'])
            # Ensure 'Amount' is numeric
            self.df['Amount'] = pd.to_numeric(self.df['Amount'], errors='coerce')
            # Drop rows with missing crucial data
            self.df.dropna(subset=['Date', 'Amount', 'Category'], inplace=True)
            print("[SUCCESS] Data successfully loaded and cleaned.")
        except FileNotFoundError:
            print(f"[ERROR] File not found at {self.data_path}")
            return False
        return True

    def generate_category_analysis(self):
        """Analyzes expenses by category and saves a bar chart."""
        category_summary = self.df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
        
        # Save Report
        category_summary.to_csv(os.path.join(self.reports_dir, "category_summary.csv"), header=["Total_Spent"])
        
        # Visualization
        plt.figure(figsize=(10, 6))
        sns.barplot(x=category_summary.values, y=category_summary.index, palette="viridis", hue=category_summary.index, legend=False)
        plt.title('Total Spending by Category')
        plt.xlabel('Amount ($)')
        plt.ylabel('Category')
        plt.tight_layout()
        plt.savefig(os.path.join(self.images_dir, 'category_bar_chart.png'))
        plt.close()
        print("[SUCCESS] Category analysis complete. Report and chart saved.")

    def generate_monthly_trend(self):
        """Analyzes monthly spending trends and saves a line chart."""
        # Extract Month-Year for grouping
        self.df['Month_Year'] = self.df['Date'].dt.to_period('M').astype(str)
        monthly_summary = self.df.groupby('Month_Year')['Amount'].sum()
        
        # Save Report
        monthly_summary.to_csv(os.path.join(self.reports_dir, "monthly_summary.csv"), header=["Total_Spent"])
        
        # Visualization
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=monthly_summary.index, y=monthly_summary.values, marker="o", color="coral", linewidth=2.5)
        plt.title('Monthly Spending Trend')
        plt.xlabel('Month')
        plt.ylabel('Total Amount ($)')
        plt.xticks(rotation=45)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()
        plt.savefig(os.path.join(self.images_dir, 'monthly_trend_line.png'))
        plt.close()
        print("[SUCCESS] Monthly trend analysis complete. Report and chart saved.")

    def generate_payment_method_analysis(self):
        """Analyzes preferred payment methods and saves a pie chart."""
        payment_summary = self.df.groupby('Payment_Method')['Amount'].sum()
        
        # Visualization
        plt.figure(figsize=(8, 8))
        colors = sns.color_palette('pastel')[0:len(payment_summary)]
        plt.pie(payment_summary.values, labels=payment_summary.index, colors=colors, autopct='%.1f%%', startangle=140)
        plt.title('Spending by Payment Method')
        plt.savefig(os.path.join(self.images_dir, 'payment_method_pie.png'))
        plt.close()
        print("[SUCCESS] Payment method analysis complete. Chart saved.")

    def generate_daily_trend(self):
        """Analyzes daily spending over time."""
        daily_summary = self.df.groupby('Date')['Amount'].sum()
        
        # Visualization
        plt.figure(figsize=(12, 5))
        sns.lineplot(x=daily_summary.index, y=daily_summary.values, color="teal", alpha=0.8)
        plt.title('Daily Spending Over Time')
        plt.xlabel('Date')
        plt.ylabel('Amount ($)')
        plt.tight_layout()
        plt.savefig(os.path.join(self.images_dir, 'daily_trend.png'))
        plt.close()
        print("[SUCCESS] Daily trend analysis complete. Chart saved.")

    def print_financial_insights(self):
        """Prints high-level financial insights to the console."""
        total_spent = self.df['Amount'].sum()
        highest_category = self.df.groupby('Category')['Amount'].sum().idxmax()
        highest_category_amt = self.df.groupby('Category')['Amount'].sum().max()
        avg_daily = total_spent / self.df['Date'].nunique()
        
        print("\n" + "="*40)
        print("= FINANCIAL INSIGHTS REPORT")
        print("="*40)
        print(f"= Total Spending: ${total_spent:,.2f}")
        print(f"~ Highest Spending Category: {highest_category} (${highest_category_amt:,.2f})")
        print(f"- Average Daily Spending: ${avg_daily:,.2f}")
        print("="*40 + "\n")

if __name__ == "__main__":
    analyzer = ExpenseAnalyzer()
    if analyzer.load_and_clean_data():
        analyzer.generate_category_analysis()
        analyzer.generate_monthly_trend()
        analyzer.generate_payment_method_analysis()
        analyzer.generate_daily_trend()
        analyzer.print_financial_insights()
