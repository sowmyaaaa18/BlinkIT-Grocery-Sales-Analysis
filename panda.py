import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("BLINKIT GROCERY SALES ANALYSIS")

print("Pandas:", pd.__version__)
print("NumPy:", np.__version__)

print("All libraries imported successfully!")
# Load BlinkIT Dataset
df = pd.read_excel("BlinkIT Grocery Data.xlsx")

# Display first 5 rows
print(df.head())
# STEP 7: Understand Dataset

print("\n--- DATASET INFORMATION ---")

# Total rows and columns
print("Dataset Shape:", df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Dataset information
print("\nDataset Info:")
df.info()

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())