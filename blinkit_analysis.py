import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load Dataset
df = pd.read_excel("BlinkIT Grocery Data.xlsx")

print("Dataset Loaded Successfully!")
# Understand Dataset

print("\n--- DATASET INFORMATION ---")

print("Dataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Info:")
df.info()

print("\nStatistical Summary:")
print(df.describe())
# STEP 8: Missing Values Analysis

print("\n--- MISSING VALUES ANALYSIS ---")

# Check missing values
print(df.isnull().sum())

# Total missing values
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# Missing percentage
print("\nMissing Values Percentage:")
print((df.isnull().sum() / len(df)) * 100)
# STEP 9: Handle Missing Values

print("\n--- HANDLING MISSING VALUES ---")

# Fill missing Item Weight using mean
mean_weight = df["Item Weight"].mean()

df["Item Weight"] = df["Item Weight"].fillna(mean_weight)

print("Missing values filled successfully!")

# Check missing values again
print("\nRemaining Missing Values:")
print(df.isnull().sum())
# STEP 10: Duplicate Values Analysis

print("\n--- DUPLICATE VALUES ANALYSIS ---")

# Check duplicate records
duplicates = df.duplicated().sum()

print("Total Duplicate Records:", duplicates)

# Remove duplicate records
df = df.drop_duplicates()

print("Duplicates Removed Successfully!")

# Check again
print("Remaining Duplicates:", df.duplicated().sum())
# STEP 11: Sales Analysis

print("\n--- SALES ANALYSIS ---")

# Total Sales
total_sales = df["Sales"].sum()
print("Total Sales:", round(total_sales, 2))

# Average Sales
average_sales = df["Sales"].mean()
print("Average Sales:", round(average_sales, 2))

# Maximum Sales
maximum_sales = df["Sales"].max()
print("Maximum Sales:", round(maximum_sales, 2))

# Minimum Sales
minimum_sales = df["Sales"].min()
print("Minimum Sales:", round(minimum_sales, 2))
# STEP 12: Item Type Sales Analysis

print("\n--- ITEM TYPE SALES ANALYSIS ---")

item_sales = df.groupby("Item Type")["Sales"].sum().sort_values(ascending=False)

print(item_sales)

# Create Bar Chart
plt.figure(figsize=(12, 6))

item_sales.plot(kind="bar")

plt.title("Sales by Item Type")
plt.xlabel("Item Type")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# STEP 14: Outlet Location Type Sales Analysis

location_sales = df.groupby("Outlet Location Type")["Sales"].sum().sort_values(ascending=False)

print("\nSales by Outlet Location Type:")
print(location_sales)

plt.figure(figsize=(8, 5))
location_sales.plot(kind="bar")

plt.title("Sales by Outlet Location Type")
plt.xlabel("Outlet Location Type")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# STEP 16: Outlet Establishment Year Analysis

year_sales = df.groupby("Outlet Establishment Year")["Sales"].sum().sort_index()

print("\nSales by Outlet Establishment Year:")
print(year_sales)

plt.figure(figsize=(10, 5))
year_sales.plot(kind="line", marker="o")

plt.title("Sales by Outlet Establishment Year")
plt.xlabel("Establishment Year")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()
# STEP 17: Item Rating Analysis

rating_analysis = df.groupby("Rating")["Sales"].mean()

print("\nAverage Sales by Item Rating:")
print(rating_analysis)

plt.figure(figsize=(8, 5))
rating_analysis.plot(kind="bar")

plt.title("Average Sales by Item Rating")
plt.xlabel("Rating")
plt.ylabel("Average Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# STEP 18: Item Visibility Analysis

visibility_sales = df.groupby("Item Type")["Item Visibility"].mean().sort_values(ascending=False)

print("\nAverage Item Visibility by Item Type:")
print(visibility_sales)

plt.figure(figsize=(12, 6))
visibility_sales.plot(kind="bar")

plt.title("Average Item Visibility by Item Type")
plt.xlabel("Item Type")
plt.ylabel("Average Item Visibility")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# STEP 19: Correlation Analysis

numeric_data = df.select_dtypes(include=np.number)

correlation = numeric_data.corr()

print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(10, 7))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
# STEP 20: Item Fat Content Sales Analysis

fat_sales = df.groupby("Item Fat Content")["Sales"].sum().sort_values(ascending=False)

print("\nSales by Item Fat Content:")
print(fat_sales)

plt.figure(figsize=(8, 5))
fat_sales.plot(kind="bar")

plt.title("Sales by Item Fat Content")
plt.xlabel("Item Fat Content")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# STEP 21: Sales Distribution Analysis

plt.figure(figsize=(10, 5))

plt.hist(df["Sales"], bins=30, edgecolor="black")

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
# STEP 22: Top 10 Best-Selling Items

top_items = df.groupby("Item Identifier")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Best-Selling Items:")
print(top_items)

plt.figure(figsize=(10, 6))
top_items.sort_values().plot(kind="barh")

plt.title("Top 10 Best-Selling Items")
plt.xlabel("Total Sales")
plt.ylabel("Item Identifier")
plt.tight_layout()
plt.show()
# STEP 23: Bottom 10 Low-Selling Items

bottom_items = df.groupby("Item Identifier")["Sales"].sum().sort_values().head(10)

print("\nBottom 10 Low-Selling Items:")
print(bottom_items)

plt.figure(figsize=(10, 6))
bottom_items.sort_values().plot(kind="barh")

plt.title("Bottom 10 Low-Selling Items")
plt.xlabel("Total Sales")
plt.ylabel("Item Identifier")
plt.tight_layout()
plt.show()
# STEP 24: Final Business Insights

print("\n========== FINAL BUSINESS INSIGHTS ==========")

print("\n1. Total Sales:", round(df["Sales"].sum(), 2))

print("\n2. Average Sales:", round(df["Sales"].mean(), 2))

print("\n3. Highest Selling Item Type:")
print(df.groupby("Item Type")["Sales"].sum().idxmax())

print("\n4. Best Performing Outlet Type:")
print(df.groupby("Outlet Type")["Sales"].sum().idxmax())

print("\n5. Best Performing Outlet Location:")
print(df.groupby("Outlet Location Type")["Sales"].sum().idxmax())

print("\n6. Highest Rated Items:")
print(df.groupby("Item Type")["Rating"].mean().idxmax())

print("\n========== ANALYSIS COMPLETED ==========")
# STEP 25: Export Cleaned Dataset

df.to_csv("BlinkIT_Cleaned_Data.csv", index=False)

print("\nCleaned dataset exported successfully!")
print("File Name: BlinkIT_Cleaned_Data.csv")
# STEP 26: Final Dataset Validation

print("\n========== FINAL DATASET VALIDATION ==========")

print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

print("\nMissing Values:")
print(df.isnull().sum().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nDataset Preview:")
print(df.head())

print("\nDATA VALIDATION COMPLETED!")