# Week 4 Assignment: MessyCorp Pandas

Read the full assignment on the HYF Data Track: [Assignment: MessyCorp Pandas](https://hub.hackyourfuture.nl/)

## Where to start

| File | Task |
|---|---|
| `src/ingest.py` | Task 1 (download inputs) and Task 7 (upload results) |
| `src/clean.py` | Task 2 (explore) and Task 3 (clean sales) |
| `src/transform.py` | Task 4 (join customers, add `is_high_value`) |
| `src/report.py` | Task 5 (build report tables) and Task 6 (write outputs) |
| `main.py` | Pipeline runner — no edits needed |
| `AI_ASSIST.md` | Task 8 — fill in before submitting |

## Setup

```bash
pip install pandas azure-identity azure-storage-blob matplotlib pyarrow
```

Log in to Azure (reuses your Week 2 session):

```bash
az login
```

## Running the pipeline

```bash
python main.py
```

This downloads inputs from Azure, cleans and transforms them, writes reports to `output/`, and uploads results back to Azure.

`data/` and `output/` are excluded from git — they are generated at runtime.

## Submitting

1. Create a branch `week4/your-name`.
2. Commit your work.
3. Push and open a Pull Request.
