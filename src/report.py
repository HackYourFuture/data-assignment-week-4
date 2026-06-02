"""Tasks 5 and 6: Build report tables and write outputs."""
import logging
from pathlib import Path

import pandas as pd


def build_reports(enriched: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Task 5: Build four summary tables using groupby and named aggregations."""

    df = enriched.copy()

    # Add revenue column (best practice)
    df["revenue"] = df["price"] * df["quantity"]

    # Add week column
    df["week"] = df["date"].dt.isocalendar().week

    # 1. Weekly revenue by region
    weekly_revenue = df.groupby(["week", "region"]).agg(
        total_revenue=("revenue", "sum"),
        order_count=("transaction_id", "count")
    ).reset_index()

    # 2. Customer summary
    customer_summary = df.groupby("customer_email").agg(
        customer_name=("customer_name", "first"),
        region=("region", "first"),
        loyalty_tier=("loyalty_tier", "first"),
        total_spent=("revenue", "sum"),
        avg_order=("revenue", "mean"),
        order_count=("transaction_id", "count")
    ).reset_index()

    # 3. Category performance
    category_performance = df.groupby("category").agg(
        total_revenue=("revenue", "sum"),
        order_count=("transaction_id", "count")
    ).reset_index()

    # 4. Loyalty analysis
    loyalty_analysis = df.groupby("loyalty_tier").agg(
        avg_spent=("revenue", "mean"),
        customer_count=("customer_email", "nunique")
    ).reset_index()

    logging.info("Reports built successfully")

    return {
        "weekly_revenue": weekly_revenue,
        "customer_summary": customer_summary,
        "category_performance": category_performance,
        "loyalty_analysis": loyalty_analysis
    }


def write_outputs(reports: dict[str, pd.DataFrame], output_dir: Path) -> None:
    """Task 6: Write report tables to CSV/Parquet and save a bar chart."""

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    output_dir.mkdir(exist_ok=True)

    # Save CSV files
    reports["weekly_revenue"].to_csv(output_dir / "weekly_revenue.csv", index=False)
    reports["category_performance"].to_csv(output_dir / "category_performance.csv", index=False)

    # Save Parquet file
    reports["customer_summary"].to_parquet(output_dir / "customer_summary.parquet", index=False)

    # Sort for visualization
    cat = reports["category_performance"].sort_values("total_revenue", ascending=False)

    # Plot bar chart
    cat.plot(
        kind="bar",
        x="category",
        y="total_revenue",
        title="Revenue by category"
    )

    # Save figure
    plt.savefig(output_dir / "category_revenue.png", bbox_inches="tight")

    logging.info("Outputs written successfully")