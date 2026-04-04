#  Phase 4A – Bucketing & Segmentation (PySpark)

##  Objective
Understand how continuous data (like total spend) can be converted into categories such as Gold, Silver, and Bronze using different segmentation techniques.

---

##  Problem Summary

- Load customer and sales data  
- Clean data (remove nulls, duplicates, invalid values)  
- Calculate total spend per customer  
- Apply multiple segmentation methods  
- Compare different segmentation approaches  
- Analyze customer distribution  

---

##  Approach

- Loaded datasets into PySpark DataFrames  
- Cleaned data by removing null values and duplicates  
- Calculated total spend per customer  
- Created customer_name for better readability  
- Applied different segmentation techniques:
  - Conditional logic  
  - Quantile-based segmentation  
  - Bucketizer method  
  - Window-based ranking  
- Compared results from all methods  

---

##  Key Transformations

- Aggregation (`sum`) to calculate total spend  
- Joins between customers and sales  
- Conditional logic (`when`)  
- Quantile calculation (`approxQuantile`)  
- Bucketizer (ML-based binning)  
- Window functions (`percent_rank`)  

---

##  Output

### 🔹 Base Dataset (Customer Spend)
Shows each customer along with their total spending.  
This is the foundation for all segmentation methods.

---

### 🔹 Conditional Segmentation  
Customers are divided using fixed rules:
- Gold → spend > 10000  
- Silver → 5000–10000  
- Bronze → < 5000  

This method is simple and based on business-defined thresholds.

---

### 🔹 Segment Distribution  
Displays the number of customers in each segment.  
Helps understand how customers are distributed across categories.

---

### 🔹 Quantile-Based Segmentation  
Customers are divided based on data distribution (top 33%, middle 33%, bottom 33%).  
This ensures balanced groups and adapts to the dataset automatically.

---

### 🔹 Bucketizer Segmentation  
Uses predefined ranges to assign customers into buckets.  
It is more structured and commonly used in machine learning pipelines. :contentReference[oaicite:0]{index=0}

---

### 🔹 Window-Based Segmentation  
Uses ranking (percentile) to divide customers into segments.  
This method assigns segments based on relative position among all customers.

---

### 🔹 Comparison of All Methods  
Shows how each segmentation method classifies the same customer differently.  
Helps understand the strengths and differences of each approach.

---

##  Learnings

- Segmentation simplifies complex data into categories  
- Different methods give different results based on logic  
- Fixed rules are simple but may not adapt to data changes  
- Quantile and ranking methods are more dynamic  
- Choosing the right method depends on business needs :contentReference[oaicite:1]{index=1}  

---

##  Reflection

- Continuous values are converted into categories for easier decision-making  
- Business segmentation uses fixed rules, while technical methods adapt to data  
- Fixed thresholds may fail when data distribution changes  
- Quantile methods ensure balanced segmentation  
- In real-world projects, a mix of methods may be used  

---