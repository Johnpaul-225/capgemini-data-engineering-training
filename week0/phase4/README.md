#  Phase 4 – Business Pipeline & Analytics

##  Objective
Build a complete end-to-end data pipeline using PySpark to generate meaningful business insights from customer and sales data.

---

##  Problem Summary

- Read customer and sales data from CSV files  
- Perform data cleaning (handle nulls, duplicates, invalid values)  
- Join datasets using customer_id  
- Calculate business metrics (daily sales, revenue, customer spend)  
- Identify key insights (top customers, repeat customers, segmentation)  
- Build a final reporting table  

---

##  Approach

- Loaded datasets into PySpark DataFrames  
- Cleaned data by removing null keys, duplicates, and invalid values  
- Created customer_name by combining first and last name  
- Applied aggregations for sales and revenue  
- Joined datasets to generate business insights  
- Built a final reporting table combining all metrics  

---

##  Key Transformations

- Data cleaning (dropna, duplicate removal, filtering invalid amounts)  
- Column transformation (creating customer_name)  
- Joins between customers and sales  
- Aggregations (sum, count)  
- Sorting and limiting results  
- Conditional logic for segmentation (Gold, Silver, Bronze)  

---

##  Output

### 🔹 Daily Sales  
Shows total sales for each day.  
Helps track business performance over time and identify trends in daily revenue.

---

### 🔹 City-wise Revenue  
Displays total revenue generated from each city.  
Helps understand which locations are performing well and contributing the most to the business.

---

### 🔹 Top 5 Customers  
Lists the top 5 customers based on their total spending.  
Helps identify the most valuable customers for the business.

---

### 🔹 Repeat Customers  
Identifies customers who have placed more than one order.  
Helps measure customer loyalty and retention.

---

### 🔹 Customer Segmentation  
Customers are divided into categories based on total spending:  
- Gold → High-value customers (spend > 10000)  
- Silver → Medium-value customers (5000–10000)  
- Bronze → Low-value customers (< 5000)  

This helps businesses target customers with personalized strategies.

---

### 🔹 Final Reporting Table  
A combined dataset containing:
- Customer name  
- City  
- Total spend  
- Order count  
- Customer segment  

This serves as a complete report for business analysis and decision-making.

---

##  Learnings

- Building a complete ETL pipeline  
- Importance of cleaning data before processing :contentReference[oaicite:0]{index=0}  
- Using joins to combine multiple datasets  
- Applying business logic using aggregations and conditions  
- Converting raw data into actionable insights  

---

##  Reflection

- Cleaning is required before joining to avoid incorrect results  
- Null keys can break joins and lead to missing data  
- Join order affects performance and output  
- Large datasets require optimization techniques  
- SQL logic and PySpark transformations follow similar concepts  

---