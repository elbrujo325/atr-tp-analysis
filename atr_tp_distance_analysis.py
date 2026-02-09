import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

sns.set_style("whitegrid")

# ==========================================================
# 1. CARGAR DATOS
# ==========================================================
file_path = r"C:\Users\TRADE08\Desktop\TRADES FOREX INDICES\PORTAFOLIO.csv"
df = pd.read_csv(file_path, sep=";")

print("\nColumnas detectadas:")
print(df.columns.tolist())

# ==========================================================
# 2. LIMPIAR COLUMNAS NUMÉRICAS
# ==========================================================
numeric_cols = ["Profit/Loss", "MAE ($)", "MFE ($)", "Time in trade"]

for col in numeric_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )

df["Profit/Loss"] = pd.to_numeric(df["Profit/Loss"], errors="coerce")
df["MAE ($)"] = pd.to_numeric(df["MAE ($)"], errors="coerce")
df["MFE ($)"] = pd.to_numeric(df["MFE ($)"], errors="coerce")

# ==========================================================
# 3. FUNCIÓN ROBUSTA PARA DURACIÓN
# ==========================================================
def convert_duration(t):
    t = str(t).replace(" ", "")
    horas = re.search(r"(\d+)h", t)
    mins  = re.search(r"(\d+)m", t)
    segs  = re.search(r"(\d+)s", t)
    h = int(horas.group(1)) if horas else 0
    m = int(mins.group(1))  if mins  else 0
    s = int(segs.group(1))  if segs  else 0
    return h + m/60 + s/3600

df["Duration"] = df["Time in trade"].apply(convert_duration)

# ==========================================================
# 4. CONVERTIR OPEN TIME A FECHA
# ==========================================================
df["Open time"] = pd.to_datetime(df["Open time"], errors="coerce")

print("\nFechas no convertidas:", df["Open time"].isna().sum())

# ==========================================================
# 5. DEFINIR STOP LOSS
# ==========================================================
STOP_LOSS = -100
UMBRAL = 5

df["Cerca_SL"] = df["Profit/Loss"] <= STOP_LOSS + UMBRAL
df_loss_near = df[df["Cerca_SL"]]

print(f"\nPérdidas cerca del SL: {len(df_loss_near)} trades")

# ==========================================================
# 6. GRAFICAS
# ==========================================================

# 6.1 Distribución MAE
plt.figure(figsize=(10,6))
sns.histplot(df_loss_near["MAE ($)"], bins=20, kde=True)
plt.axvline(STOP_LOSS, color="red", linestyle="--")
plt.title("Distribución de MAE ($) en pérdidas cerca del SL")
plt.xlabel("MAE ($)")
plt.show()

# 6.2 MFE vs MAE
plt.figure(figsize=(10,6))
plt.scatter(df_loss_near["MAE ($)"], df_loss_near["MFE ($)"], c="yellow", edgecolors="black")
plt.axvline(STOP_LOSS, color="red", linestyle="--")
plt.title("MFE vs MAE en pérdidas cercanas al Stop Loss")
plt.xlabel("MAE ($)")
plt.ylabel("MFE ($)")
plt.show()

# 6.3 Duración
plt.figure(figsize=(10,6))
sns.histplot(df_loss_near["Duration"], bins=20, kde=True, color="orange")
plt.title("Duración (horas) de trades que perdieron cerca del SL")
plt.xlabel("Horas")
plt.show()

# 6.4 Hora del día
df_loss_near = df_loss_near[df_loss_near["Open time"].notna()]
df_loss_near["Hora"] = df_loss_near["Open time"].dt.hour

plt.figure(figsize=(10,6))
sns.histplot(df_loss_near["Hora"], bins=24)
plt.title("Hora de apertura de trades que pierden cerca del SL")
plt.xlabel("Hora del día")
plt.show()

# 6.5 Close type
plt.figure(figsize=(10,6))
df_loss_near["Close type"].value_counts().plot(kind="bar", color="yellow", edgecolor="black")
plt.title("Tipo de cierre de pérdidas cercanas al SL")
plt.ylabel("Cantidad")
plt.show()
