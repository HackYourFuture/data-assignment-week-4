# Week 4 Assignment: MessyCorp Pandas

**Clean and report on messy sales data** · Total: 100 points · Passing: 60

Read the full assignment on the HYF Data Track: [Assignment: MessyCorp Pandas](https://hub.hackyourfuture.nl/)

---

## Where to start

Work through the files in this order:

| Step | File | Tasks |
|---|---|---|
| 1 | `src/ingest.py` | Task 1: download inputs from Azure |
| 2 | `src/clean.py` | Task 2: explore + Task 3: clean sales |
| 3 | `src/transform.py` | Task 4: join customers, add `is_high_value` |
| 4 | `src/report.py` | Task 5: build report tables + Task 6: write outputs |
| 5 | `src/ingest.py` | Task 7: upload results to Azure |
| 6 | `main.py` | Set `GITHUB_USERNAME`, then run the full pipeline |
| 7 | `AI_ASSIST.md` | Task 8: fill in before submitting |

Open each file and read the docstrings and TODO comments — they explain exactly what to implement.

---

## Repository layout

```text
.
├── src/
│   ├── ingest.py       # Tasks 1 + 7 — Azure download and upload
│   ├── clean.py        # Tasks 2 + 3 — explore and clean sales data
│   ├── transform.py    # Task 4     — join customers, add is_high_value
│   └── report.py       # Tasks 5 + 6 — build tables and write outputs
├── main.py             # Pipeline runner — set GITHUB_USERNAME for Task 7
├── AI_ASSIST.md        # Task 8 — fill in before submitting
├── .gitignore          # data/ and output/ are excluded — generated at runtime
└── .hyf/
    └── test.sh         # auto-grader — read this to see exactly what is checked
```

Files the pipeline generates at runtime (gitignored):
- `data/` — raw CSVs downloaded from Azure in Task 1
- `output/` — report CSVs, Parquet, and chart written in Task 6

---

## Setup

```bash
pip install pandas azure-identity azure-storage-blob matplotlib pyarrow
```

Log in to Azure (reuses your Week 2 session):

```bash
az login
```

> **If Task 1 is blocked** (Azure login issues, no network): manually copy `messy_sales.csv` and `messy_customers.csv` into a `data/` folder at the repo root, then comment out the `download_inputs` call in `main.py`. You can complete Tasks 2–6 without Azure access and return to Tasks 1 and 7 once your session is working.

---

## Run the pipeline

Edit `GITHUB_USERNAME` in `main.py` before running Task 7, then:

```bash
python main.py
```

---

## Check your score locally

Run the same grader the auto-grader runs on every PR push:

```bash
bash .hyf/test.sh
cat .hyf/score.json
```

---

## Scoring ladder

Points accumulate as you complete each task. Partial credit is awarded within each level.

| Score | What the grader checks |
|---|---|
| 14 | Function stubs committed (all five `def` names present, Azure imports, `data/` in `.gitignore`) |
| ~24 | Task 2 done: `.info()`, `.describe()`, `.isna().sum()`, `.head()` all called |
| ~44 | Task 3 done: vectorized string cleaning, `pd.to_numeric`, `pd.to_datetime`, row filters, `drop_duplicates` on `transaction_id` |
| ~59 | Task 4 done: email normalisation, `how="inner"` merge, vectorised `is_high_value` |
| ~79 | Task 5 done: named aggregations (`total_revenue=`, `order_count=`), `isocalendar().week`, `("customer_name", "first")` |
| ~89 | Task 6 done: all three output files written with `index=False`, chart saved |
| ~94 | Task 7 done: `upload_outputs` uses `assert` + `len()` to verify the round-trip |
| 100 | Code quality: `Path(...)` constructor used in `src/`, `logging.info/warning/error` calls present |

---

## Submitting

1. Create a branch `week4/your-name`.
2. Commit your work.
3. Push and open a Pull Request.
