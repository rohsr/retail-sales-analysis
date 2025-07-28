import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


sns.set(style="whitegrid")  

df = pd.read_csv('./data/superstore.csv', encoding='latin1')



print(df.head())
print("\nColumns:"  , df.columns.tolist())


# Cleaning the data

df.drop_duplicates(inplace=True)

# Convert 'Order Date' and 'Ship Date' to datetime

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())


# Extract Month and Year from trend analysis

df['Order Month'] = df['Order Date'].dt.to_period('M')

# Monthly sales trend
monthly_sales = df.groupby('Order Month')['Sales'].sum().reset_index()
monthly_sales['Order Month'] = monthly_sales['Order Month'].dt.to_timestamp()

# Plotting the monthly sales trend
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Order Month', y='Sales', marker='o')
plt.title('Monthly Sales Trend')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./images/monthly_sales_trend.png')
plt.show()


# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
region_sales.plot(kind='bar', color='skyblue')
plt.title('Sales by Region')    
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('./images/sales_by_region.png')
plt.show()


# Profit by Product Category + Sub-Category

category_profit = df.groupby(['Category', 'Sub-Category'])['Profit'].sum().sort_values()

plt.figure(figsize=(14, 8))
category_profit.plot(kind='barh', color='salmon')
plt.title('Profit by Product Category and Sub-Category')
plt.xlabel('Total Profit')
plt.tight_layout()
plt.savefig('./images/profit_by_category.png') 
plt.show()


# Top 10 Customers by Sales
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10 )

plt.figure(figsize=(12, 6))
top_customers.plot(kind='bar', color='green')
plt.title('Top 10 Customers by Sales')
plt.xlabel('Total Sales')
plt.gca().invert_yaxis()  # Invert y-axis to show top customer first
plt.tight_layout()
plt.savefig('./images/top_customers_by_sales.png')
plt.show()


