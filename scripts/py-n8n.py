import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

try:
    # Generate sample data
    np.random.seed(42)  # For reproducibility

    # Create dates for the last 30 days
    dates = [datetime.now() - timedelta(days=x) for x in range(30)]

    # Create sample data
    data = {
        'Date': dates,
        'Sales': np.random.randint(1000, 5000, size=30),
        'Customers': np.random.randint(50, 200, size=30),
        'Product_ID': np.random.randint(1, 100, size=30),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], size=30),
        'Revenue': np.random.uniform(1000, 10000, size=30).round(2)
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Sort by date
    df = df.sort_values('Date', ascending=False)

    # Save to Excel file
    excel_filename = 'demo_data12.xlsx'
    
    # Get the full path
    current_dir = os.getcwd()
    full_path = os.path.join(current_dir, excel_filename)
    
    print(f"Attempting to save file to: {full_path}")
    
    # Save the file
    df.to_excel(excel_filename, index=False, sheet_name='Sales Data')
    
    # Verify the file was created
    if os.path.exists(excel_filename):
        print(f"Excel file '{excel_filename}' has been created successfully!")
        print(f"File size: {os.path.getsize(excel_filename)} bytes")
    else:
        print("Error: File was not created!")

    print("\nFirst few rows of the data:")
    print(df.head())

except Exception as e:
    print(f"An error occurred: {str(e)}")