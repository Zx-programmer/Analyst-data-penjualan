import pandas as pd 
import matplotlib.pyplot as plt

#Source Data
df = pd.read_csv('e-commerce_sell.csv')

#Analisa Data
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum()) 
df["TotalSales"] = ( df["UnitPrice"] * df["Quantity"] * (1-df["DiscountApplied"]))
print(df[["ProductID", "UnitPrice", "Quantity", "DiscountApplied", "TotalSales"]])
average_sales = df[["TotalSales"]].mean()
print("Rata rata penjualan:" ,average_sales)
product_sales = df.groupby("ProductID")[["TotalSales"]].sum()
product_sales = product_sales.sort_values(by="TotalSales", ascending=False)
print(product_sales)

#Visualisasi Data
product_sales = df.groupby("ProductID")[["TotalSales"]].sum()
product_sales = product_sales.sort_values(by="TotalSales", ascending=False)

product_sales.plot(kind="bar")
plt.title("Total Penjualan per produk")
plt.xlabel("Produk")
plt.ylabel("Total Penjualan")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
