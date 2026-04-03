-- =========================================
-- ETL PIPELINE: CUSTOMERS + SALES (SQL)
-- =========================================

-- 1. CLEAN DATA (USING CTEs)

WITH sales_clean AS (
    SELECT *
    FROM sales
    WHERE customer_id IS NOT NULL
      AND quantity IS NOT NULL
      AND total_amount IS NOT NULL
      AND quantity > 0
      AND total_amount > 0
),

customers_clean AS (
    SELECT *
    FROM customers
    WHERE customer_id IS NOT NULL
),

-- 2. JOIN DATA

joined AS (
    SELECT s.*, c.city
    FROM sales_clean s
    JOIN customers_clean c
    ON s.customer_id = c.customer_id
),

-- 3. DAILY SALES
daily_sales AS (
    SELECT sale_date, SUM(total_amount) AS daily_sales
    FROM sales_clean
    GROUP BY sale_date
),

-- 4. CITY REVENUE
city_revenue AS (
    SELECT city, SUM(total_amount) AS revenue
    FROM joined
    GROUP BY city
),

-- 5. REPEAT CUSTOMERS (>2 orders)
repeat_customers AS (
    SELECT customer_id, COUNT(*) AS order_count
    FROM sales_clean
    GROUP BY customer_id
    HAVING COUNT(*) > 2
),

-- 6. CUSTOMER SPEND PER CITY
customer_spend AS (
    SELECT city, customer_id, SUM(total_amount) AS total_spent
    FROM joined
    GROUP BY city, customer_id
),

-- 7. TOP CUSTOMER PER CITY
top_customers AS (
    SELECT city, customer_id, total_spent
    FROM (
        SELECT *,
               ROW_NUMBER() OVER (PARTITION BY city ORDER BY total_spent DESC) AS rank
        FROM customer_spend
    ) t
    WHERE rank = 1
),

-- 8. FINAL REPORT
final_report AS (
    SELECT customer_id, city,
           SUM(total_amount) AS total_spend,
           COUNT(*) AS order_count
    FROM joined
    GROUP BY customer_id, city
)

-- FINAL OUTPUTS

SELECT * FROM daily_sales;

SELECT * FROM city_revenue;

SELECT * FROM repeat_customers;

SELECT * FROM top_customers;

SELECT * FROM final_report;