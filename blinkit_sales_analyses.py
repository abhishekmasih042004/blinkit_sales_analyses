import pandas as pd
df = pd.read_excel("C:\Users\Public\Documents\Shell Extension\\blinkit_sales_data.xlsx")
print(df.head())
print("blinkit data all info")
print(df.info())
print('check duplicates values')
print(df.duplicated().sum())
print(df.describe())
""" 5 Highest Products Months Comparison"""
print("5 Highest Products Months Comparison")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["year_Month"] = df["Order_Date"].dt.to_period('M')
top5_products = (
    df.groupby('Product') ["Quantity"]
    .sum()
    .nlargest(5)
    .index
    )
df_top5 = df[df["Product"].isin(top5_products)]

grouped = (
    df_top5
    .groupby(["year_Month","Product"]) ["Quantity"]
    .sum()
    .reset_index()
    )
pivot_table = grouped.pivot_table(
    index = 'year_Month',
    columns = 'Product',
    values = "Quantity",
    fill_value = 0
    )
print(pivot_table)
"""customers repeat Anlayse """

print("customers repeat Anlayse")

"""unique customers count code """

unique_customer = df["Customer_ID"].nunique()

print("unique customers count",unique_customer)

""" How many times each customers has visited code """

customer_count = df["Customer_ID"].value_counts()

print("\nOder count per customers(Top 10):")

print(customer_count.head(10))

"""Repeat customers who have ordered more than once code"""

Repeat_customer = customer_count[customer_count > 1]

print ("\nNumber of repeat coustomers",Repeat_customer.shape[0])

"""Repeat customer list only code"""
Repeat_customer_list = Repeat_customer.index.tolist()

print("Repeat customer list (Top 10 ID):")
for cid in Repeat_customer_list[:10]:
    print(cid)

""" Q1 How many order come in daily.
    Q2 How many order come in weekly.
    Q3 Which days have the most order. code """

print("\nQ1 How many order come in daily"
      "\nQ2 How many order come in weekly"
     "\nQ3 Which days have the most order")

""" order date column ko date format mai convert karna""" 

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

""" daily orders volume nikalna """

daily_orders = df.groupby(df["Order_Date"].dt.date)["Order_ID"].count().reset_index()
daily_orders.columns = ["Date" , "Total_Orders"]

""" weekly orders volume nikalna """

weekly_orders = df.groupby(df["Order_Date"].dt.week)["Order_ID"].count().reset_index()
weekly_orders.columns = ["weekly_Number","Total_Orders"]

""" Which days have the most order """

busiest_index = daily_orders["Total_Orders"].idxmax()
busiest_day = daily_orders.iloc[busiest_index]

"""" output print ara hu """

print("Daily orders:")
print(daily_orders.head())
print("\nweekly orders:")
print(weekly_orders.head())
print("\nDay with the most orders:")
print(busiest_day)

print("High-value customers list top 10 spenders")

""" High-value customers list top 10 spenders """

""" oreder_date ko date_time mai convert karna code """

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

""" customer wise total kharch nikalna code """

customer_spending = df.groupby("Customer_ID")["Total_Sales"].sum().reset_index()

""" columns ko nama dara hu code """

customer_spending.columns=["Customer_ID","Total_Spending"]

""" spending ko descending order mai sort kara hu code"""

high_value_customer = customer_spending.sort_values(by="Total_Spending",ascending = False)

""" output print kara hun code """
print(high_value_customer.head(10))
















    





    


 






