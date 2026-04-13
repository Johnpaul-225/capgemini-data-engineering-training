#  Advanced Data Pipeline – Car Sales (SQL + PySpark)

##  Objective
Build a complete data engineering pipeline using PySpark for transformations and SQL for analysis.

The goal is to process car sales data, perform cleaning, validation, and generate business insights including dealer performance and customer behavior.

---

##  Problem Summary

- Load multiple datasets (customers, cars, sales, dealers)  
- Clean and validate data  
- Handle nulls, duplicates, and invalid values  
- Perform transformations and aggregations  
- Analyze dealer and customer performance  
- Use SQL for advanced analytics  
- Generate final outputs  

---

##  Dataset Used

- customers → customer details  
- cars → car information  
- sales → sales transactions  
- dealers → dealer details  
- sales_dealer → mapping between sales and dealers  

---

##  Approach

1. Loaded all datasets into PySpark DataFrames  
2. Checked schema and data quality  
3. Cleaned data (nulls, invalid values, duplicates)  
4. Validated foreign key relationships  
5. Performed transformations and aggregations  
6. Built dealer-level analytics  
7. Used SQL for advanced queries  
8. Generated final outputs  

---

##  Key Transformations

- Data cleaning (null handling, duplicates removal)  
- Filtering invalid records  
- Joins across multiple tables  
- Aggregations (sum, count)  
- Grouping by customer, city, brand, dealer  
- SQL queries for analytics  

---

##  Output / Results

### 🔹 Data Understanding
- Loaded all datasets  
- Checked schema and row counts  
- Identified missing and invalid data  

---

### 🔹 Data Cleaning
- Handled null values  
- Fixed incorrect data (e.g., negative prices)  
- Trimmed string columns  
- Removed invalid records  

---

### 🔹 Data Validation
- Checked foreign key relationships  
- Identified invalid records using joins  
- Created validation report  

---

### 🔹 Customer Insights
- Calculated total revenue per customer  
- Identified high-value customers  

---

### 🔹 Sales Analysis
- Brand-wise sales performance  
- City-wise revenue distribution  

---

### 🔹 Dealer Analytics
- Revenue per dealer  
- Top-performing dealers  
- Contribution of dealers by city  

---

### 🔹 SQL Analysis
- Top 3 customers per city  
- Monthly sales trends  
- Repeat customers  

---

### 🔹 Final Output
- Clean and transformed datasets  
- Aggregated business reports  
- Ready for analysis and decision-making  

---

##  Learnings

- How to build end-to-end ETL pipelines  
- Importance of data cleaning and validation  
- Working with multi-table datasets  
- Combining PySpark and SQL effectively  
- Generating business insights from data  

---

##  Reflection

- Data validation is critical before analysis  
- Joins must be handled carefully  
- SQL is powerful for analysis  
- PySpark is efficient for large-scale data processing  

---


##  Final Outcome

This project demonstrates:

End-to-end pipeline building  
Data cleaning and validation  
Multi-table joins and transformations  
Business analytics using SQL  
Real-world data engineering workflow  
