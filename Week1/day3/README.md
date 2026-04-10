#  SQL Practice – CASE WHEN & Window Functions

##  Objective
This project focuses on applying advanced SQL concepts like:
- Conditional logic using CASE WHEN  
- Customer behavior analysis  
- Window functions for ranking and analytics  

The goal is to simulate real-world business scenarios and generate insights from data.

---

##  Problem Summary

- Analyze telecom customer usage data  
- Apply multiple business rules using CASE WHEN  
- Categorize customers based on usage patterns  
- Implement ranking using window functions  
- Generate insights for decision-making  

---

##  Modules Covered

### 🔹 1. CASE WHEN – Business Logic (CustomerUsage)

- Plan upgrade suggestions  
- Customer classification (heavy, moderate, light users)  
- Voice usage analysis  
- Offer eligibility detection  
- Reward program allocation  
- Billing and discount suggestions  
- Usage mismatch detection  
- Customer segmentation (Gold, Silver, Bronze)  

---

### 🔹 2. Window Functions

- Assign row numbers to records  
- Rank employees based on salary  
- Perform ranking within departments  
- Use dense ranking for continuous ranking  
- Analyze order and employee data  

---

##  Approach

- Created structured tables (CustomerUsage, Employees)  
- Inserted sample data with different usage patterns  
- Applied CASE WHEN for business rule evaluation  
- Used window functions (ROW_NUMBER, RANK, DENSE_RANK)  
- Generated categorized outputs  

---

##  Key SQL Concepts Used

### 🔹 CASE WHEN
- Conditional logic  
- Nested conditions  
- Business rule implementation  

---

### 🔹 Window Functions
- ROW_NUMBER() → unique ranking  
- RANK() → ranking with gaps  
- DENSE_RANK() → ranking without gaps  

---

##  Output / Results

### 🔹 Plan Upgrade Suggestions  
Identified customers who should upgrade plans based on usage and billing.

---

### 🔹 Customer Classification  
Categorized customers as heavy, moderate, or light users based on data usage.

---

### 🔹 Voice Usage Analysis  
Classified customers as:
- Excessive talkers  
- Frequent callers  
- Normal users  

---

### 🔹 Offer Eligibility  
Detected customers eligible for:
- Combo offers  
- Cashback offers  

---

### 🔹 Reward Segmentation  
Assigned customers into:
- Gold  
- Silver  
- Bronze  
- Basic tiers  

---

### 🔹 Usage Pattern Detection  
Identified mismatched plans such as:
- Underutilized postpaid  
- Overpaying prepaid  

---

### 🔹 Advanced Customer Insights  
- Super users  
- Data-oriented users  
- Voice-oriented users  
- Balanced users  

---

### 🔹 Window Function Outputs  
- Ranked employees by salary  
- Ranked employees within departments  
- Generated row numbers for ordered data  
- Applied dense ranking for consistent ranking  

---

##  Learnings

- CASE WHEN helps implement real business logic  
- Window functions enable advanced analytics  
- Ranking functions are useful for comparisons  
- SQL can simulate real-world decision systems  
- Combining logic + analytics gives deeper insights  

---

##  Reflection

- Business rules can be complex but manageable using CASE WHEN  
- Window functions simplify ranking problems  
- Data-driven decisions require proper classification  
- SQL is powerful for both analysis and transformation  

---

##  Final Outcome

This project demonstrates the ability to:

 Apply business logic using SQL  
 Analyze customer behavior  
 Use window functions for ranking  
 Generate actionable insights  
