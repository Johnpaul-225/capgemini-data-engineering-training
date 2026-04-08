# 🧹 Data Cleaning & Standardization (PySpark)

##  Objective
Clean and standardize a messy dataset using PySpark by handling null values, duplicates, inconsistent formats, and invalid data.

---

##  Problem Summary

- Dataset contains inconsistent values (blank, mixed case, duplicates)  
- Clean and standardize text fields  
- Handle missing and invalid numeric values  
- Remove duplicates  
- Prepare final clean dataset for analysis  

---

##  Approach

- Loaded dataset with customer details  
- Identified data quality issues (nulls, duplicates, invalid values)  
- Replaced invalid values like "blank" with null  
- Standardized country names  
- Removed duplicates  
- Converted sales column to numeric  
- Filled missing values  
- Sorted final dataset  

---

##  Key Transformations

- Replaced invalid values (`blank`, `Blank` → null)  
- Standardized text using `initcap()`  
- Replaced inconsistent values (`New York` → `USA`)  
- Removed duplicate rows  
- Converted `Sales` column to integer  
- Filled null values (`Sales = 0`, `Category = UNKNOWN`)  
- Filtered unwanted records  
- Sorted dataset  

---

##  Output / Results

### 🔹 Handling Missing Values  
Replaced invalid entries like "blank" with null values.  
Ensures proper handling of missing data.

---

### 🔹 Standardizing Country Names  
Converted country names into consistent format (e.g., `india` → `India`).  
Improves data consistency for analysis.

---

### 🔹 Fixing Inconsistent Data  
Replaced incorrect values like `New York` with `USA`.  
Ensures uniform location data.

---

### 🔹 Removing Duplicates  
Duplicate records (like repeated customer entries) were removed.  
Prevents incorrect aggregations.

---

### 🔹 Cleaning Sales Column  
Converted Sales column into numeric format.  
Invalid values were replaced with null and later filled with 0.

---

### 🔹 Filling Missing Values  
- Missing Sales → replaced with 0  
- Missing Category → replaced with "UNKNOWN"  

Ensures no null values remain.

---

### 🔹 Filtering Data  
Removed specific unwanted records (CustomerID = 104).  
Helps clean incorrect or duplicate entries.

---

### 🔹 Final Dataset  
Sorted clean dataset by CustomerID.  
Now ready for further analysis or pipeline processing.

---

##  Learnings

- Real-world data is often messy and inconsistent  
- Data cleaning is essential before analysis  
- Standardizing text fields improves data quality  
- Handling null and invalid values prevents errors  
- Duplicate removal is critical for accurate results  

---

##  Reflection

- Without cleaning, analysis results would be incorrect  
- Small inconsistencies (like case differences) can cause major issues  
- Data validation should always be part of the pipeline  
- Clean data leads to better business decisions  

---
  