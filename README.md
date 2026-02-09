# ATR TP Distance Analysis

This project analyzes how well a trading strategy places its Take Profit (TP)
levels by comparing the **intended TP price** with the **maximum favorable
movement (MFE)** that each trade actually experienced in the market.

The objective is to quantify **how far the TP is from what the market realistically
offered**, and evaluate whether missed profits are caused by poor entries or by
overly ambitious TP placement.

## Motivation
A strategy can have good entries and correct market direction, yet still underperform
if the Take Profit is systematically placed too far from the price action.

This analysis focuses on answering a key question:

> *Did the market move in favor of the trade, but fail to reach the Take Profit?*

## Methodology
For each trade, the script:
- Computes the Average True Range (ATR) from historical OHLC data
- Reconstructs theoretical TP and SL levels using ATR multiples
- Measures the Market Favorable Excursion (MFE) and Adverse Excursion (MAE)
- Computes the distance between the TP and the actual MFE
- Expresses TP distance as both price and percentage of entry
- Identifies and filters trades with excessively distant TP levels
- Compares performance metrics before and after filtering

## Analysis Outputs
- Complete trade-level analysis (CSV)
- Filtered trade dataset excluding unrealistic TP placements
- Equity curves before and after filtering
- Statistical comparison of performance metrics
- Visual dashboard summarizing the full analysis

## Use Case
This tool is designed as a **post-trade diagnostic system**, useful for:
- Evaluating TP placement quality
- Improving risk/reward calibration
- Refining strategy exits without modifying entry logic

## Tech Stack
- Python
- pandas
- numpy
- matplotlib

## Disclaimer
This is **not a backtest** and does not generate trading signals.
It is a post-trade analytical tool intended for strategy evaluation and refinement.
