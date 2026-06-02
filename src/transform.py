"""Task 4: Join customer data and add derived columns."""
import logging

import pandas as pd
def join_customers(sales: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    """Task 4: Normalize join keys, merge, and add a derived boolean flag."""

    # Create copies to avoid modifying original DataFrames
    sales = sales.copy()
    customers = customers.copy()

    # Normalize join keys (email) to ensure consistent matching
    sales["customer_email"] = sales["customer_email"].str.lower().str.strip()
    customers["customer_email"] = customers["customer_email"].str.lower().str.strip()

    # Perform inner join between sales and customers on customer_email
    merged = sales.merge(
        customers,
        on="customer_email",
        how="inner"
    )

    # Create high-value flag based on revenue per transaction (vectorized operation)
    merged["is_high_value"] = (merged["price"] * merged["quantity"]) >= 150

    logging.info("Customers joined successfully")

    return merged