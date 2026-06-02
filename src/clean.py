"""Tasks 2 and 3: Explore and clean the raw DataFrames."""
import logging
from pathlib import Path

import pandas as pd

def load_and_explore(data_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Task 2: Load both CSV files and explore their contents before cleaning."""

    sales = pd.read_csv(data_dir / "messy_sales.csv")
    customers = pd.read_csv(data_dir / "messy_customers.csv")

    # INFO
    print("\nSALES INFO")
    print(sales.info())

    print("\nCUSTOMERS INFO")
    print(customers.info())

    # DESCRIBE
    print("\nSALES DESCRIBE")
    print(sales.describe())

    # HEAD
    print("\nSALES HEAD")
    print(sales.head(20))

    print("\nCUSTOMERS HEAD")
    print(customers.head(20))

    # MISSING VALUES
    print("\nSALES MISSING VALUES")
    print(sales.isna().sum())

    print("\nCUSTOMERS MISSING VALUES")
    print(customers.isna().sum())

    logging.info("Exploration completed")

    return sales, customers

def clean_sales(sales: pd.DataFrame) -> pd.DataFrame:
    """Task 3: Clean the sales DataFrame using vectorized Pandas operations."""

    sales = sales.copy()

    # clean product_name and customer_email with vectorized string methods
    sales["product_name"] = sales["product_name"].str.strip().str.title()
    sales["customer_email"] = sales["customer_email"].str.lower().str.strip()

    # convert types
    sales["price"] = pd.to_numeric(sales["price"], errors="coerce")
    sales["date"] = pd.to_datetime(sales["date"], errors="coerce")

    # remove rows with missing or invalid critical values
    sales = sales.dropna(subset=["product_name"])
    sales = sales[sales["price"] >= 0]
    sales = sales[sales["quantity"] > 0]
    sales = sales.dropna(subset=["date"])

    # remove duplicate transactions, keeping the first occurrence
    sales = sales.drop_duplicates(subset="transaction_id", keep="first")

    logging.info("Sales cleaned successfully")

    return sales
