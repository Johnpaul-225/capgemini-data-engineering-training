--querie 1
SELECT customer_id,SUM(total_amount) AS total_order_amount
FROM sales
GROUP BY customer_id;

--querie 2
SELECT customer_id,SUM(total_amount) AS total_spend
FROM sales
GROUP BY customer_id
ORDER BY total_spend DESC
LIMIT 3;

--querie 3
SELECT c.*
FROM customers c
LEFT JOIN sales s
ON c.customer_id = s.customer_id
WHERE s.customer_id IS NULL;

--querie 4
SELECT c.city,SUM(s.total_amount) AS total_revenue
FROM customers c
JOIN sales s
ON c.customer_id = s.customer_id
GROUP BY c.city
ORDER BY total_revenue DESC;

--querie 5
SELECT customer_id,AVG(total_amount) AS avg_order_amount
FROM sales
GROUP BY customer_id;

--querie 6
SELECT customer_id,COUNT(*) AS order_count
FROM sales
GROUP BY customer_id
HAVING COUNT(*) > 1;

--querie 7
SELECT customer_id,SUM(total_amount) AS total_spend
FROM sales
GROUP BY customer_id
ORDER BY total_spend DESC;