import pandas as pd
import os

# Step 1: Load raw data
df = pd.read_csv("../data/sales_data_raw.csv")
print("🔍 Original Columns:")
print(df.columns)

# Step 2: Drop columns that are not useful
df.drop(columns=['rating.count', 'rating.rate'], inplace=True, errors='ignore')

# Step 3: Rename columns for consistency
df.rename(columns={
    'title': 'product_name',
    'price': 'price_usd',
    'category': 'product_category',
    'description': 'product_description'
}, inplace=True)

# Step 4: Add new feature: discounted price (assume 10% discount)
df['discounted_price'] = df['price_usd'] * 0.9

# Step 5: Save cleaned data
df.to_csv("../data/sales_data_cleaned.csv", index=False)
print("✅ Cleaned data saved to data/sales_data_cleaned.csv")

# Optional: Show top 5
print(df.head())
