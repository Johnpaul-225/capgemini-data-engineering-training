#  Phase 5 – Databricks + Olist End-to-End Pipeline

##  Objective
Build a complete end-to-end data engineering pipeline using a real-world dataset (Olist E-commerce).  
This phase focuses on ingestion, joining multiple tables, applying advanced analytics, and generating business insights.

---

##  Problem Summary

- Load multiple datasets (orders, customers, products, payments, order_items)  
- Validate and inspect data  
- Join multiple tables to create a unified dataset  
- Apply aggregations and window functions  
- Generate advanced business insights  
- Build a final reporting table  

---

##  Approach

- Loaded all datasets into Spark DataFrames  
- Inspected schema and checked missing values  
- Joined multiple tables to form a fact dataset  
- Applied aggregations to calculate metrics  
- Used window functions for ranking and running totals  
- Built final reporting dataset  

---

##  Key Transformations

- Joins (multiple table joins)  
- Aggregations (`sum`, `count`, `countDistinct`)  
- Window functions (`row_number`, `dense_rank`, running total)  
- Date transformation (`to_date`)  
- Conditional logic for segmentation  

---

##  Output

### 🔹 Top 3 Customers per City  
Shows the top 3 customers in each city based on total spending.  
Helps identify high-value customers in every location.

---

### 🔹 Running Total of Sales  
Displays daily sales along with cumulative (running) total over time.  
Helps track business growth and overall revenue trend.

---

### 🔹 Top Product per Category  
Identifies the best-selling product in each category.  
Helps understand which products perform best within each category.

---

### 🔹 Customer Lifetime Value (LTV)  
Calculates total spending of each customer across all orders.  
Helps measure long-term value of customers.

---

### 🔹 Customer Segmentation  
Customers are grouped into:
- Gold → High spenders  
- Silver → Medium spenders  
- Bronze → Low spenders  

Also shows number of customers in each segment.  
Helps in targeted marketing and business strategy.

---

### 🔹 Final Reporting Table  
A combined dataset containing:
- Customer ID  
- City  
- Total spend  
- Segment  
- Total orders  

This acts as a complete business report for decision-making.

---

##  Learnings

- Working with real-world multi-table dataset :contentReference[oaicite:0]{index=0}  
- Understanding fact and dimension tables  
- Importance of validating joins  
- Using window functions for advanced analytics  
- Building a complete data pipeline  

---

##  Reflection

- Window functions help in ranking and cumulative calculations  
- Joining multiple tables requires careful validation  
- Real-world data pipelines are more complex than simple queries  
- Proper data modeling improves performance and clarity  
- ETL pipelines are essential for business insights  

---