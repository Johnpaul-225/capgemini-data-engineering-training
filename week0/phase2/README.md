#  Phase 2 – Data Processing

##  Problem Understanding

The objective of this phase is to process and analyze customer and sales data using Apache Spark.
The dataset consists of two main files:

* **Customers Dataset** – contains customer details such as name, location, and contact information.
* **Sales Dataset** – contains transaction details like product purchased, quantity, and total amount.

The goal is to perform data analysis operations such as aggregation, filtering, and joining to extract meaningful insights.

---

##  Approach Taken

To solve the problem, PySpark was used for distributed data processing. The approach includes:

1. Loading CSV data into Spark DataFrames
2. Cleaning data (handling null values)
3. Applying transformations such as:

   * GroupBy and Aggregations
   * Joins between datasets
   * Filtering and sorting
4. Generating insights like total revenue, top customers, and average order values

---

##  Transformations

### 1. Data Loading

* Loaded datasets using Spark CSV reader with headers and schema inference.

### 2. Data Cleaning

* Removed null values using `dropna()` for important columns like `customer_id`.

### 3. Data Processing

Performed the following operations:

*  Total order amount per customer
*  Top 3 customers by total spend
*  Customers with no orders
*  City-wise total revenue
*  Average order amount per customer
*  Customers with more than one order
*  Sorting customers by total spend

### 4. Joins

* Used **inner join** and **left join** to combine customer and sales data.

---

##  Results / Insights

* Identified top customers contributing highest revenue
* Found customers who have not placed any orders
* Analyzed revenue distribution across cities
* Calculated average spending behavior of customers

---

##  Learnings

* Understanding of distributed data processing using PySpark
* Hands-on experience with DataFrame operations
* Learned aggregation, joins, and filtering techniques
* Importance of schema handling and data cleaning

---

##  Challenges Faced

* Data type issues (e.g., string vs numeric for total_amount)
* Understanding difference between PySpark functions and Python functions
* Debugging aggregation and join operations

---


##  Conclusion

This phase helped in building strong fundamentals of big data processing using Apache Spark. It demonstrated how large datasets can be efficiently processed and analyzed to generate business insights.
