# Data Science Learning Lab

An original interactive lesson in data summaries, grouped means, and correlation
using a small, fictional built-in study-practice dataset.

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

The example data is synthetic, small, and for practicing analysis only; its
correlations do not establish causation. Run tests with
`python -m unittest discover -s tests -v`.
