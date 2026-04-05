#  Phase 1 – SQL to PySpark Foundations

##  Objective
Understand basic SQL queries and their equivalent PySpark operations.  
This phase builds a strong foundation for working with DataFrames and simple data transformations.

---

##  Problem Summary

- Create a simple customer table  
- Perform basic SQL queries  
- Convert SQL queries into PySpark DataFrame operations  
- Practice filtering, selecting, and grouping data  

---

##  Approach

- Created a small dataset with customer details  
- Executed basic SQL queries on the table  
- Recreated the same dataset in PySpark  
- Applied equivalent PySpark transformations  
- Compared SQL vs PySpark results  

---

##  Key Transformations

- Displaying data (`show`)  
- Filtering rows (`WHERE` → `filter`)  
- Selecting columns (`SELECT` → `select`)  
- Aggregation (`GROUP BY` → `groupBy`)  

---

##  Output

### 🔹 Show All Customers  
Displays all records in the dataset.  
Helps verify that the data is loaded correctly.

---

### 🔹 Customers from Chennai  
Filters and shows only customers who belong to Chennai.  
Helps understand how to apply conditions on data.

---

### 🔹 Customers with Age > 25  
Shows customers whose age is greater than 25.  
Used to filter data based on numeric conditions.

---

### 🔹 Selected Columns (Name & City)  
Displays only specific columns (customer name and city).  
Helps in reducing unnecessary data and focusing on required fields.

---

### 🔹 Customer Count per City  
Groups data by city and counts number of customers in each city.  
Helps understand distribution of customers across locations.

---

##  Learnings

- SQL and PySpark follow similar logic :contentReference[oaicite:0]{index=0}  
- DataFrame works like a table  
- Filtering and selecting are basic but important operations  
- Aggregations help summarize data  

---

##  Reflection

- SQL is easier to read, PySpark is better for large-scale data  
- Understanding basics is important before moving to advanced topics  
- These operations are building blocks for ETL pipelines  

---
