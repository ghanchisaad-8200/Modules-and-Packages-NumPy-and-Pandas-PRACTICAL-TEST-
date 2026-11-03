# Python Lab Practical Test (Units 7 & 8)

This repository contains my solutions for the **Python Units 7 & 8 Lab Practical Test (Set C)**. All the work is done in a single Jupyter Notebook, `PRACTICAL_TEST.ipynb`, divided into four sections.

## Topics Covered

| Section | Questions | Topics |
|---|---|---|
| **A** | Q1 - Q3 | `datetime` / `timedelta`, `math`, `random`, `uuid`, `time` |
| **B** | Q4 - Q6 | `os` and `shutil`, custom module (`unitconv`), `__name__` guard, package and sub-package (`bankkit`) |
| **C** | Q7 - Q10 | NumPy: array creation, slicing, boolean masks, `np.where`, views vs copies, array maths and statistics, reshape, broadcasting, splitting |
| **D** | Q11 - Q15 | Pandas: Series and DataFrame, data cleaning, filtering, `loc` / `iloc`, categories, `groupby`, pivot table, merge, JSON |

## Project Structure

```
.
├── PRACTICAL_TEST.ipynb   # Main notebook with all solutions (Sections A to D)
├── unitconv.py            # Custom module (Q5)
├── bankkit/               # Package with sub-package (Q6)
│   ├── __init__.py
│   ├── interest.py
│   ├── fees.py
│   └── reports/
│       ├── __init__.py
│       └── statement.py
├── agents.csv             # Dataset: delivery agents (Section D)
├── supervisors.csv        # Dataset: zone supervisors (Section D)
├── names.json             # Output file created in Q15
└── README.md
```

> The `bankkit/` folder and `unitconv.py` are created by the notebook itself using `%%writefile`, so they appear after running the relevant cells.

## Dataset (Section D)

**`agents.csv`** has delivery agents of a courier company with columns `AgentID, Name, Zone, City, StartDate, Pay, Incentive`. It deliberately contains data problems that are fixed during cleaning:

- one duplicate row (Agent 405)
- one missing `Pay` value (Agent 404)
- the text `pending` inside the numeric `Incentive` column

**`supervisors.csv`** maps each `Zone` to its `Supervisor`. The zone `Central` exists only in this file, which shows the difference between inner and outer merges.

## Requirements

- Python 3.9 or higher
- Jupyter Notebook or JupyterLab
- NumPy
- pandas

Install the libraries with:

```bash
pip install numpy pandas notebook
```

## How to Run

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```
2. Start Jupyter:
   ```bash
   jupyter notebook
   ```
3. Open `PRACTICAL_TEST.ipynb` and run the cells **from top to bottom** (Kernel > Restart & Run All).

Important notes:

- Run the cells in order. Section D builds on the same DataFrame (`df`), so the cleaning in Q12 carries into Q13 - Q15.
- Run the notebook from the same folder that holds `agents.csv` and `supervisors.csv`.
- To see the `unitconv.py` guard message, run `python unitconv.py` directly. When it is imported, the message does not appear.

## Key Concepts Practiced

- Working with dates, times, UUIDs and random numbers using the standard library
- File and folder handling with `os` and `shutil`
- Creating custom modules and packages, and the three import styles
- NumPy indexing, masking, broadcasting and statistics
- Pandas data cleaning, grouping, pivot tables, merging and JSON input/output

## Author

saad
