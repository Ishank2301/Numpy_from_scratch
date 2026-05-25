# NumPy from Scratch

A small, hands-on NumPy notebook in plain Python files. The goal is simple:
learn the pieces that keep showing up in machine learning work without hiding
them behind a big project structure.

The examples are intentionally short and runnable one by one. They cover array
creation, indexing, slicing, broadcasting, filtering, aggregate functions,
random number generation, and a few warm-up Python problems.

## Setup

Use Python 3.11+ and a current NumPy release.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -e .
```

Run any lesson directly:

```powershell
python .\Array-numpy1.py
python .\Broadcasting-numpy.py
python .\Random_no.py
```

## Files

| File | Topic |
| --- | --- |
| `Array-numpy1.py` | Basic array edits and arithmetic |
| `Agrregate-fn.py` | Sum, mean, spread, min/max, and axis operations |
| `Broadcasting-numpy.py` | Shape rules and row/column expansion |
| `Filtering.py` | Boolean masks and conditional replacement |
| `Numpy-operation.py` | A clean two-sum practice problem |
| `operations-list-adv.py` | Multidimensional indexing and slicing |
| `Random_no.py` | Modern random generation with `default_rng` |
| `Scalar_numpy.py` | Scalar math, vectorized functions, comparisons |
| `practise.py` | A tiny slicing warm-up |

## Notes

These files are written like learning notes, not library modules. Keeping the
output labelled makes it easier to run a script, compare the result, and move on
to the next NumPy idea.
