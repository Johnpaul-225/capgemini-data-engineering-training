#  Phase 6 – Spark Playground Exit Sprint (Advanced Practice Lab)

##  Objective
Build strong confidence in PySpark by practicing joins, window functions, date operations, and complete ETL pipeline execution.

This phase focuses on preparing for real-world data engineering tasks and transitioning to Databricks.

---

##  Problem Summary

- Work with dirty datasets (customers & orders)  
- Clean data (nulls, duplicates, invalid values)  
- Validate foreign key relationships  
- Perform joins between datasets  
- Apply aggregations (total spend, order count)  
- Use window functions for ranking  
- Perform date-based analysis  
- Build and execute a complete pipeline  

---

##  Dataset Used

### 🔹 Customers Table
- customer_id  
- name  
- email  
- city  

Issues:
- Null values (name, email)  
- Extra spaces in names  

---

### 🔹 Orders Table
- order_id  
- customer_id  
- order_date  
- amount  

Issues:
- Negative values  
- Null amount  
- Invalid foreign key (customer_id = 99)  
- Duplicate-like records  

---

##  Approach

1. Created DataFrames with sample dirty data  
2. Converted date column to proper format  
3. Cleaned datasets (nulls, invalid values, trimming)  
4. Validated data using joins  
5. Joined customers and orders  
6. Applied aggregations (spend, order count)  
7. Used window functions for ranking  
8. Generated final output dataset  

---

##  Key Transformations

- Removed null values  
- Trimmed string columns  
- Filtered negative amounts  
- Handled missing values  
- Used **left_anti join** to find invalid foreign keys  
- Performed joins between datasets  
- Aggregations:
  - Total spend  
  - Order count  
- Window functions:
  - Ranking customers by spend  
- Date conversion using `to_date()`  

---

##  Output / Results

### 🔹 Data Cleaning
- Removed invalid records (nulls, negative values)  
- Standardized customer names  
- Ensured data consistency  

---

### 🔹 Data Validation
- Identified invalid customer_id using left_anti join  
- Removed records with no matching customer  

---

### 🔹 Joined Dataset
- Combined customers and orders  
- Created a unified dataset for analysis  

---

### 🔹 Customer Spend Analysis
- Calculated total spend per customer  
- Counted number of orders per customer  

---

### 🔹 Ranking Customers
- Ranked customers based on total spend  
- Identified top-performing customers  

---

### 🔹 Date Analysis
- Converted string to date format  
- Enabled time-based analysis (daily/monthly trends)  

---

### 🔹 Final Output
- Cleaned and transformed dataset  
- Ready for reporting and analytics  
- Saved output for further use  

---

##  Learnings

- Improved fluency in PySpark transformations  
- Strong understanding of joins (inner, left, left_anti)  
- Hands-on experience with window functions  
- Importance of data validation  
- Ability to debug and fix data issues  
- Built confidence in creating full pipelines  

---

##  Reflection

- Data cleaning takes the most time but is critical  
- Debugging joins helped understand data relationships  
- Window functions simplified ranking problems  
- Now able to build pipelines independently  
- Need to improve speed and optimization  

---


##  Final Outcome

This phase demonstrates:

End-to-end ETL pipeline building  
Data cleaning and validation  
Joins and transformations  
Window function usage  
Readiness for Databricks  
