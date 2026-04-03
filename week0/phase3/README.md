#  Phase 3 – Final ETL & Pipeline (PySpark)

##  Objective
Build an end-to-end ETL pipeline using PySpark to process customer and sales data and generate meaningful business insights.

---

##  Problem Summary

- Read customer and sales data from CSV files  
- Perform data cleaning (handle nulls and duplicates)  
- Join datasets using customer_id  
- Calculate key metrics (total spend, average order, etc.)  
- Identify business insights (top customers, repeat customers)  
- Generate final outputs for reporting  

---

##  Approach

- Loaded datasets into PySpark DataFrames  
- Inspected schema and sample data  
- Cleaned data by removing nulls and duplicates  
- Joined datasets using customer_id  
- Applied aggregations and filters  
- Generated final outputs  

---

##  Key Transformations

- Data cleaning using dropna and duplicate removal  
- Filtering invalid records (amount > 0)  
- Joins (inner and left join)  
- Aggregations (sum, avg, count)  
- Sorting and limiting results  

---

##  Output

### 🔹 Total Spend Per Customer  
This shows the total amount spent by each customer across all their purchases.  
It helps identify high-value customers who contribute the most to overall revenue.

---

### 🔹 Top 3 Customers  
This lists the top 3 customers based on their total spending.  
It is useful for identifying the most important customers for the business.

---

### 🔹 Customers With No Orders  
This identifies customers who have not made any purchases.  
It helps in finding inactive users who can be targeted through marketing campaigns.

---

### 🔹 Revenue Per City  
This shows the total revenue generated from each city.  
It helps understand which locations are performing well and contributing more to the business.

---

### 🔹 Average Order Amount  
This calculates the average amount spent per order by each customer.  
It helps analyze customer spending behavior and purchase patterns.

---

### 🔹 Repeat Customers  
This identifies customers who have placed more than one order.  
It helps measure customer loyalty and retention.

---

##  Learnings

- Understanding ETL process (Extract → Transform → Load)  
- Importance of data cleaning  
- Using joins to combine datasets  
- Applying aggregations for insights  
- Building an end-to-end data pipeline  
