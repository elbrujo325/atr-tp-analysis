# 🎯 ATR Take Profit Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE) [![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)

**MFE/MAE analysis — measures how far Take Profit is from what the market actually offered**

---

## 📝 Overview

Analyzes whether a trading strategy's Take Profit levels are well-placed by comparing the intended TP price with the Maximum Favorable Excursion (MFE) — the best price the trade actually reached. Identifies trades where the market moved in favor but couldn't reach the TP, and filters out excessively distant TP placements.

## 🔑 Key Features

- **ATR-based TP and SL level reconstruction**
- **Maximum Favorable Excursion (MFE) computation**
- **Maximum Adverse Excursion (MAE) computation**
- **TP-MFE distance analysis (absolute and percentage)**
- **Excessive TP distance filtering**
- **Before/after performance comparison**


## 🚀 Quick Start

```bash
git clone https://github.com/elbrujo325/atr-tp-analysis.git
cd atr-tp-analysis

pip install pandas numpy matplotlib yfinance

python atr_tp_analysis.py
```

Output: CSV with trade-level analysis including MFE, MAE, TP distance, and filtered performance metrics.

## 🛠️ Tech Stack

Python · Pandas · NumPy · Matplotlib · yfinance

## 📄 License

This project is licensed under the MIT License — see [LICENSE](./LICENSE) for details.

---

<div align="center">

*By [Henry Paolo Alfaro Sotil](https://github.com/elbrujo325) — Physicist & Data Scientist*

</div>
