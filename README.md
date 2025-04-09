 # Retail Sales Analysis (EDA using Python)

📌 Project Overview

This project performs Exploratory Data Analysis (EDA) on retail sales data using Python (pandas, NumPy, Matplotlib, Seaborn). The objective is to analyze sales trends, customer purchasing behavior, and identify key insights to improve business decisions.

📂 Dataset
The dataset includes retail sales transactions with the following columns:

Order ID, Order Date, Product Name, Quantity Ordered, Price Each, Purchase Address, Total Sales

🛠️ Technologies Used
Python (pandas, NumPy)

Data Visualization (Matplotlib)

Pycharm

📊 Key Analysis & Insights
# ✔ Data Cleaning & Preprocessing:

Removed missing values and duplicates.

Converted data types for better analysis.

Extracted city names from purchase addresses for regional insights.

# ✔ Feature Engineering:

Created a Total Sales column (Quantity Ordered * Price Each).

Extracted Month, Day, and Time from Order Date for trend analysis.

# ✔ Exploratory Data Analysis (EDA):

Monthly Sales Trend: Identified peak sales months.

Best-Selling Products: Found top-selling items and their revenue contribution.

City-Wise Sales: Determined high-performing locations.

Peak Order Hours: Identified 6 PM - 8 PM as the busiest shopping hours.

Frequently Bought Together Products: Used itertools.combinations to find common product pairs.

# ✔ Data Visualization:

Line Chart: Monthly sales trends.

Bar Chart: Best-selling products.

Heatmap: Orders by hour of the day.

Pie Chart: Sales distribution by city.

🚀 Key Findings

✅ December had the highest sales, likely due to holiday shopping.

✅ Phones & Laptops were top-selling products, indicating a strong tech-savvy customer base.

✅ Most purchases occurred between 6 PM - 8 PM, useful for sales optimization.

✅ Customers frequently bought complementary products together, ideal for cross-selling strategies.
