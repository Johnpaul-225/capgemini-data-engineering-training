Phase 3 – Final ETL & Pipeline (PySpark)
Objective

This phase focuses on building a complete ETL pipeline using PySpark.
The goal is to read raw data, clean it, apply transformations, and generate useful business insights like customer spending, top customers, and city-wise revenue.

Problem Statement (Summary)
Read customer and sales data from CSV files
Perform data cleaning (handle null values and duplicates)
Join multiple datasets using common keys
Calculate important metrics like total spend and average order
Identify business insights (top customers, repeat customers, etc.)
Generate final outputs for reporting

Detailed problem statement is available in: phase3_problem_statement.pdf

Dataset Used
Dataset: Customers & Sales Sample Data
Source: Spark Playground (/samples/)
Tables Used:
customers
sales
Approach
Loaded customer and sales data into PySpark DataFrames
Inspected data using preview and schema
Cleaned data by removing null values and duplicates
Joined datasets using customer_id
Applied business logic and aggregations
Generated final outputs for analysis
Key Transformations
Data cleaning (dropna, removing duplicates)
Filtering invalid records (e.g., negative or zero amounts)
Joins (inner join, left join)
Aggregations (sum, avg, count)
Sorting and limiting results
Output

This pipeline generates several useful business insights:

🔹 Total Spend Per Customer

Shows how much each customer has spent in total.
Helps identify high-value customers and their contribution to revenue.

🔹 Top 3 Customers

Displays the top 3 customers based on total spending.
Useful for identifying the most important customers for the business.

🔹 Customers With No Orders

Lists customers who have not made any purchases.
Helps identify inactive users for potential marketing efforts.

🔹 Revenue Per City

Shows total revenue generated from each city.
Helps understand which locations perform best.

🔹 Average Order Amount

Displays the average amount spent per order by each customer.
Helps analyze customer spending behavior.

🔹 Repeat Customers

Identifies customers who placed more than one order.
Helps measure customer loyalty and retention.

Final Outcome

The pipeline converts raw data into meaningful insights that help in:

Identifying valuable customers
Improving marketing strategies
Understanding regional performance
Analyzing customer behavior
Challenges Faced
Handling missing and inconsistent data
Understanding join operations correctly
Filtering only valid transactions
Designing the pipeline in proper ETL flow
Learnings
Understanding ETL process (Extract → Transform → Load)
Importance of data cleaning before analysis
Using joins to combine multiple datasets
Applying aggregations for business insights
Building an end-to-end data pipeline
📁 Files in this Folder
phase3_problem_statement.pdf → Problem description
solution.py / notebook → Implementation