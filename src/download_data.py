import logging
from pathlib import Path
from azure.identity import InteractiveBrowserCredential
from azure.storage.blob import BlobServiceClient

ACCOUNT_URL = "https://sthyfstudentsdemo.blob.core.windows.net"
SOURCE_CONTAINER = "week4-inputs"
FILES = ["messy_sales.csv", "messy_customers.csv"]

credential = InteractiveBrowserCredential()

service = BlobServiceClient(account_url=ACCOUNT_URL, credential=credential)
container = service.get_container_client(SOURCE_CONTAINER)

Path("data").mkdir(exist_ok=True)

for name in FILES:
    blob = container.get_blob_client(name)
    with open(f"data/{name}", "wb") as f:
        f.write(blob.download_blob().readall())
    logging.info("Downloaded %s", name)
    