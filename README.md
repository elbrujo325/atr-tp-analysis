> ⚠️ **Este repositorio fue consolidado y mejorado en [smallcap-quant-ml](https://github.com/elbrujo325/smallcap-quant-ml). Se conserva aquí por historial.**

---

# ATR Take Profit Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)

**MFE/MAE analysis of Take Profit placement — measures distance between TP and actual market favorable excursion**

---

## 📋 Overview

Analyzes whether a trading strategy's Take Profit levels are well-placed by comparing intended TP prices with the Maximum Favorable Excursion (MFE) the market actually offered. Identifies trades where TP was too conservative, well-placed, or excessively distant.

### Key Metrics
- **TP-MFE Distance** (absolute & %) — How far TP was from maximum favorable move
- **Excessive TP Filtering** — Flags trades where TP was unreachable
- **Before/After Performance** — Comparison of filtered vs unfiltered results
- **Time-of-Day Analysis** — Hourly distribution of TP quality

---

## 🚀 Quick Start

```bash
git clone https://github.com/elbrujo325/atr-tp-analysis.git
cd atr-tp-analysis
pip install pandas numpy matplotlib seaborn
# Place backtest results CSV in project root
python atr_tp_distance_analysis.py
```

---

## 📊 Required Data Format

CSV with columns (semicolon-separated):
- `Profit/Loss` — Trade PnL
- `MAE ($)` — Maximum Adverse Excursion
- `MFE ($)` — Maximum Favorable Excursion
- `Time in trade` — Duration (e.g., "2h 30m 15s")
- `Open time` — Entry timestamp
- `Close type` — Exit reason: SL, TP, Time Exit

Optional TP columns for full analysis:
- `TP Price` — Intended take profit level
- `Entry Price` — Entry price

---

## 📈 Outputs

- **CSVs** — Trade-level analysis with TP-MFE distances
- **Charts** — MAE distribution, MFE vs MAE scatter, duration histogram, hourly distribution, close type breakdown
- **Console** — Summary statistics

---

## ⚙️ Configuration

```python
STOP_LOSS = -100   # Your SL level in $
UMBRAL = 5         # Threshold for "near SL" filter
```

---

## 🛠️ Tech Stack

Python · Pandas · NumPy · Matplotlib · Seaborn

---

## 📄 License

MIT License — see [LICENSE](./LICENSE)

---

<div align="center">

**By Henry Paolo Alfaro Sotil — Physicist & Data Scientist**

[GitHub](https://github.com/elbrujo325) · [LinkedIn](https://linkedin.com/in/henry-paolo-alfaro-sotil-3b75a9338)

</div>
