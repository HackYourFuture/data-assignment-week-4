# AI Assist Report

## 1. Prompt I gave the LLM

During this assignment, I used an AI assistant to help me build and debug a data pipeline in Python using Pandas and Azure Blob Storage.

Example prompts I gave:

- "Help me load CSV files from Azure Blob Storage using Python"
- "How do I clean messy data using Pandas vectorized operations?"
- "How do I merge two DataFrames on email and handle missing values?"
- "How do I build groupby reports in Pandas?"
- "How do I upload files to Azure Blob Storage using DefaultAzureCredential?"

---

## 2. Code suggested by the LLM

The AI suggested several implementations, including:

- Using BlobServiceClient from azure.storage.blob to download and upload files
- Using pd.read_csv() to load datasets
- Cleaning data using:
  - .str.lower().str.strip()
  - pd.to_numeric(errors="coerce")
  - pd.to_datetime(errors="coerce")
- Joining datasets using:
  - merge(..., how="inner")
- Creating derived columns like:
  - revenue = price * quantity
  - is_high_value = revenue >= 150
- Building reports using:
  - groupby() and named aggregations
- Writing outputs using:
  - to_csv()
  - to_parquet()
  - matplotlib for visualization

---

## 3. What worked and what I changed

### What worked:
- The structure of the pipeline (ingest → clean → transform → report → export)
- Pandas vectorized operations
- Groupby aggregations for reports
- File output handling (CSV and Parquet)

### What I changed:
- I replaced Azure download with a local fallback because Azure access was not working.
- I simplified Task 7 by skipping Azure upload due to authentication issues.
- I improved data cleaning by creating a revenue column instead of using lambda functions.
- I adjusted logging messages for clarity.

---

## 4. Final notes

This project helped me understand:
- How to build a full data pipeline in Python
- How to clean real-world messy datasets
- How to use Pandas efficiently without loops
- How to structure code into modular functions

Even though Azure upload was skipped, the rest of the pipeline works successfully using local data.