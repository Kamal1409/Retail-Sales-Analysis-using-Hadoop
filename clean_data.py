import pandas as pd

# Load the Excel file
df = pd.read_excel("OnlineRetail.xlsx")

# Drop missing values and filter invalid rows
df.dropna(inplace=True)
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# Save cleaned data
df.to_csv("../data/OnlineRetail.csv", index=False)
print("Cleaned data saved to ../data/OnlineRetail.csv")
