from pyspark.sql import SparkSession
from pyspark.sql import functions as F
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
# load csv files
customers = spark.read.option("header", "true").csv("/samples/customers.csv")
sales = spark.read.option("header", "true",).option("inferSchema", "true").csv("/samples/sales.csv")
customers=customers.dropna(subset=["customer_id"])
sales=sales.dropna(subset=["customer_id"])
customers.show()
sales.show()
# query 1
sales.groupBy("customer_id").agg(F.sum("total_amount").alias("total_order_amount")).show()

# query 2
sales.groupBy("customer_id").agg(F.sum("total_amount").alias("total_spend")).orderBy("total_spend",ascending=False).limit(3).show()

# query 3
customers_no_orders = customers.join(sales,on="customer_id",how="left").filter(sales.customer_id.isNull()).show()

# query 4
customers.join(sales,"customer_id").groupBy("city").agg(F.sum("total_amount").alias("total_revenue")).orderBy("total_revenue",ascending=False).show()

# query 5
sales.groupBy("customer_id").agg(F.avg("total_amount").alias("avg_order_amount")).show()

# query 6
sales.groupBy("customer_id").agg(F.count("*").alias("order_count")).filter(F.col("order_count")>1).show()

# query 7
sales.groupBy("customer_id").agg(F.sum("total_amount").alias("total_spend")).orderBy("total_spend",ascending=False).show()