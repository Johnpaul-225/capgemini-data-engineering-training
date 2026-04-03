#  Phase 3A – Data Quality & Cleaning Challenge

##  Objective
Work with messy data and apply data cleaning techniques before building a pipeline.  
This phase helps understand why data cleaning is critical in real-world data engineering.

---

##  Problem Summary

- Identify data issues (null values, duplicates, invalid data)  
- Clean data by removing null keys and handling missing values  
- Remove duplicate records  
- Filter invalid data (e.g., negative age)  
- Validate cleaning using row counts  
- Perform aggregation (customers per city)  

---

##  Approach

- Created a DataFrame with intentionally messy data  
- Inspected schema and initial data  
- Removed rows with null customer_id  
- Filled missing values for name and city  
- Removed duplicate records  
- Filtered out invalid age values (age ≤ 0)  
- Validated results using row counts  
- Performed aggregation to count customers per city  

---

##  Key Transformations

- Dropped null values in key column (customer_id)  
- Filled missing values with default values ("Unknown")  
- Removed duplicate rows  
- Filtered invalid records (age > 0)  
- Grouped data by city and counted customers  

---

##  Output

### 🔹 Original Data
The dataset initially contained multiple issues:
- Missing customer_id values  
- Null values in name and city  
- Duplicate rows  
- Invalid age (negative value)  

This represents real-world messy data.

---

### 🔹 Cleaned Data
After applying cleaning steps:
- Rows with missing customer_id were removed  
- Missing name and city values were replaced with "Unknown"  
- Duplicate records were removed  
- Invalid age values (≤ 0) were filtered out  

The final dataset is now clean and ready for analysis.

---

### 🔹 Row Count Validation
Row count was checked before and after cleaning:
- Before cleaning → higher count (including bad data)  
- After cleaning → reduced count (only valid data)  

This confirms that incorrect and unnecessary data was removed.

---

### 🔹 Customers Per City
The final aggregation shows number of customers in each city.  
This helps understand distribution of customers across locations.

---

##  Learnings

- Real-world data is always messy  
- Data cleaning is essential before analysis  
- Missing and invalid data can lead to incorrect results  
- Validation ensures data quality  
- Aggregations should always be performed on clean data  

---

##  Reflection

- Skipping cleaning leads to wrong insights and bad decisions  
- Invalid values (like negative age) can distort analysis  
- Duplicate data can inflate counts and metrics  
- A proper cleaning checklist is important in every pipeline  