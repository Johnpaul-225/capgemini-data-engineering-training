from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# 1. Initialize Spark Session
spark = SparkSession.builder \
    .appName("Phase4_Business_Pipeline") \
    .getOrCreate()

# 2. Load Data
customers = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/samples/customers.csv")

sales = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/samples/sales.csv")

# 3. Data Cleaning
customers = customers.dropna(subset=["customer_id"]) \
                     .dropDuplicates(["customer_id"])

sales = sales.dropna(subset=["customer_id"]) \
             .dropDuplicates(["sale_id"]) \
             .filter(F.col("total_amount") > 0)

# Create customer_name
customers = customers.withColumn(
    "customer_name",
    F.concat_ws(" ", F.col("first_name"), F.col("last_name"))
)

# 4. Daily Sales
daily_sales = sales.groupBy("sale_date") \
    .agg(F.sum("total_amount").alias("total_sales"))

# 5. City-wise Revenue
city_revenue = sales.join(customers, "customer_id") \
    .groupBy("city") \
    .agg(F.sum("total_amount").alias("total_revenue"))

# 6. Top 5 Customers
top_customers = sales.join(customers, "customer_id") \
    .groupBy("customer_name") \
    .agg(F.sum("total_amount").alias("total_spend")) \
    .orderBy(F.col("total_spend").desc()) \
    .limit(5)

# 7. Repeat Customers
repeat_customers = sales.groupBy("customer_id") \
    .agg(F.count("sale_id").alias("order_count")) \
    .filter(F.col("order_count") > 1)

# 8. Customer Segmentation
customer_spend = sales.groupBy("customer_id") \
    .agg(F.sum("total_amount").alias("total_spend"))

segmentation = customer_spend.join(customers, "customer_id") \
    .withColumn(
        "segment",
        F.when(F.col("total_spend") > 10000, "Gold")
         .when((F.col("total_spend") >= 5000) & (F.col("total_spend") <= 10000), "Silver")
         .otherwise("Bronze")
    ) \
      .select("customer_name", "total_spend", "segment")

# 9. Final Reporting Table

# Step 1: base aggregation
final_report = sales.join(customers, "customer_id") \
    .groupBy("customer_id", "customer_name", "city") \
    .agg(
        F.sum("total_amount").alias("total_spend"),
        F.count("sale_id").alias("order_count")
    )

# Step 2: add segmentation
final_report = final_report.join(
    segmentation.select("customer_name", "segment"),
    on="customer_name",
    how="left"
)

# -------------------------------
# OUTPUT
# -------------------------------
final_report.show()

# 11. Display Outputs
print("----- DAILY SALES -----")
daily_sales.show()

print("----- CITY REVENUE -----")
city_revenue.show()

print("----- TOP 5 CUSTOMERS -----")
top_customers.show()

print("-----  Customer Segmentation -----")
segmentation.show()

print("----- FINAL REPORT -----")
final_report.show()