# Retail Stock Analyzer Model

A Python-based data analysis project for analyzing retail transaction data, focusing on customer segmentation, market basket analysis, and sales patterns.

## Overview

This project analyzes retail transaction data to provide insights into:
- Customer purchasing patterns and segmentation
- Product associations and market basket analysis
- Sales trends and seasonality
- Stock management recommendations

## Project Structure

```
Retail_Stock_Analyzer_Model/
├── data_loading.ipynb        # Data loading and initial validation
├── data_cleaning_and_preprocessing.ipynb  # Data cleaning pipeline
├── requirements.txt         # Python package dependencies
└── README.md               # Project documentation
```

## Requirements

### Data File
- Place `Online Retail.xlsx` in the project root directory
- Expected columns:
  - InvoiceNo: Transaction identifier
  - StockCode: Product code
  - Description: Product description
  - Quantity: Number of items
  - InvoiceDate: Date and time of transaction
  - UnitPrice: Price per unit
  - CustomerID: Customer identifier (optional for basket analysis)
  - Country: Country of sale

### Python Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

1. **Data Loading**
   - Open `data_loading.ipynb`
   - Select the project's virtual environment as kernel
   - Run all cells to load and validate the raw data

2. **Data Cleaning & Preprocessing**
   - Open `data_cleaning_and_preprocessing.ipynb`
   - Run the cleaning pipeline which handles:
     - Missing values
     - Data type conversions
     - Duplicate removal
     - Feature engineering
     - Anomaly detection


## Data Cleaning Pipeline

The preprocessing pipeline performs these steps:
1. Converts data types (dates, IDs)
2. Handles missing CustomerIDs (required for segmentation)
3. Imputes missing product descriptions
4. Removes duplicates and anomalies
5. Filters non-product items
6. Engineers features (time-based, sales calculations)
7. Computes basket metrics

## Notes

- CustomerID is required for customer segmentation but optional for market basket analysis
- Non-product codes (shipping, adjustments, etc.) are filtered out
- Cancelled orders (InvoiceNo starting with 'C') are removed
- Negative quantities and prices are excluded
- Time features are extracted for temporal analysis


## Acknowledgments

- Dataset based on retail transactions data
- Built with pandas, numpy, and seaborn for analysis