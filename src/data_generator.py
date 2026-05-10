import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_synthetic_data(output_path="data/synthetic_expenses.csv", num_records=200):
    """
    Generates synthetic personal expense data and saves it to a CSV file.
    
    Args:
        output_path (str): Path to save the generated CSV.
        num_records (int): Number of expense records to generate.
    """
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    categories = [
        "Food & Dining", "Transportation", "Housing", 
        "Utilities", "Entertainment", "Shopping", 
        "Healthcare", "Education", "Miscellaneous"
    ]
    
    payment_methods = ["Credit Card", "Debit Card", "Cash", "UPI", "Bank Transfer"]
    
    # Generate dates for the last 6 months
    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)
    
    # Generate random dates within the range
    dates = [start_date + timedelta(days=np.random.randint(0, 180)) for _ in range(num_records)]
    
    data = {
        "Date": [d.strftime("%Y-%m-%d") for d in dates],
        "Category": np.random.choice(categories, num_records, p=[0.25, 0.15, 0.20, 0.10, 0.10, 0.10, 0.05, 0.03, 0.02]),
        "Amount": np.random.uniform(5.0, 500.0, num_records).round(2),
        "Payment_Method": np.random.choice(payment_methods, num_records),
        "Description": ["Simulated expense"] * num_records
    }
    
    df = pd.DataFrame(data)
    
    # Sort by date
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date').reset_index(drop=True)
    
    # Save to CSV
    df.to_csv(output_path, index=False)
    print(f"[SUCCESS] Successfully generated {num_records} synthetic expense records at '{output_path}'.")

if __name__ == "__main__":
    generate_synthetic_data()
