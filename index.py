import pandas as pd
import numpy as np
import warnings
import os

warnings.filterwarnings('ignore')

# Load and preprocess data
def ensure_outputs_dir(base_dir: str) -> str:
    outputs_dir = os.path.join(base_dir, "outputs")
    os.makedirs(outputs_dir, exist_ok=True)
    return outputs_dir


def resolve_dataset_path() -> str:
    # Prefer explicit env var
    explicit = os.environ.get("DATA_PATH")
    if explicit and os.path.exists(explicit):
        return explicit
    # Fallback to local file next to this script
    local_path = os.path.join(os.path.dirname(__file__), 'Online Retail.xlsx')
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        return local_path
    raise FileNotFoundError("Excel dataset not found or is empty. Set DATA_PATH to the absolute path of Online Retail.xlsx.")


def load_and_preprocess_data() -> pd.DataFrame:
    """
    Load UCI Online Retail.xlsx and perform preprocessing:
    - Remove cancellations/credits
    - Keep positive Quantity and UnitPrice
    - Compute TotalPrice
    - Parse dates and derive year/month/day-of-week/hour
    - Drop rows with missing essential fields
    """
    data_path = resolve_dataset_path()
    df = pd.read_excel(data_path, engine='openpyxl')

    expected_cols = {"InvoiceNo", "StockCode", "Description", "Quantity", "InvoiceDate", "UnitPrice", "CustomerID", "Country"}
    missing = expected_cols - set(df.columns)
    if missing:
        raise ValueError(f"Dataset missing expected columns: {sorted(missing)}")

    # Remove invoices that are likely cancellations (InvoiceNo starting with 'C')
    df = df[df['InvoiceNo'].astype(str).str.startswith('C') == False]

    # Filter positive quantities and prices
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

    # Drop rows with missing critical fields
    df = df.dropna(subset=['InvoiceNo', 'StockCode', 'InvoiceDate', 'Country'])

    # Compute totals and time parts
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['InvoiceYear'] = df['InvoiceDate'].dt.year
    df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M').dt.to_timestamp()
    df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()
    df['Hour'] = df['InvoiceDate'].dt.hour

    return df.reset_index(drop=True)

def main():
    base_dir = os.path.dirname(__file__)
    outputs_dir = ensure_outputs_dir(base_dir)

    df = load_and_preprocess_data()
    print("Dataset Overview (cleaned):")
    print(f"Shape: {df.shape}")
    print(f"Date Range: {df['InvoiceDate'].min()} to {df['InvoiceDate'].max()}")

    # Save cleaned dataset
    cleaned_path = os.path.join(outputs_dir, 'online_retail_cleaned.csv')
    df.to_csv(cleaned_path, index=False)
    print(f"Saved cleaned dataset to: {cleaned_path}")


if __name__ == "__main__":
    main()
