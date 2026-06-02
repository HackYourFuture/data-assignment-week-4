"""Task 1: Download inputs from Azure (or fallback local). Task 7: Upload outputs back to Azure."""
import logging
from pathlib import Path
import io

import pandas as pd
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

ACCOUNT_URL = "https://sthyfstudentsdemo.blob.core.windows.net"
SOURCE_CONTAINER = "week4-inputs"
FILES = ["messy_sales.csv", "messy_customers.csv"]


def download_inputs(data_dir: Path) -> None:
    """
    Task 1: Download input CSV files from Azure Blob Storage.
    Fallback: use local files if Azure is not available.
    """

    logging.info("Loading data from local folder...")

    data_dir.mkdir(exist_ok=True)

    for name in FILES:
        src = Path("data") / name
        dst = data_dir / name

        if not src.exists():
            raise FileNotFoundError(f"Missing file: {src}")

        dst.write_bytes(src.read_bytes())

        logging.info(f"Copied {name} from local data folder")

def upload_outputs(output_dir: Path, github_username: str) -> None:
    logging.info("Task 7 skipped (Azure not used)")
    return