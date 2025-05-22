-- 1. Total Revenue by Product Category
SELECT p.category, SUM(s.revenue) AS total_revenue
FROM fact_sales s
JOIN dim_product p ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;

-- 2. Monthly Sales Trends
SELECT d.year, d.month, SUM(s.revenue) AS total_revenue
FROM fact_sales s
JOIN dim_date d ON s.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;

-- 3. Revenue by Region
SELECT st.region, SUM(s.revenue) AS total_revenue
FROM fact_sales s
JOIN dim_store st ON s.store_id = st.store_id
GROUP BY st.region
ORDER BY total_revenue DESC;

-- 4. Top Products by Quantity Sold
SELECT p.name AS product_name, SUM(s.quantity_sold) AS total_quantity
FROM fact_sales s
JOIN dim_product p ON s.product_id = p.product_id
GROUP BY p.name
ORDER BY total_quantity DESC
LIMIT 10;