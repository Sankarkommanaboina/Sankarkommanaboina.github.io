SELECT order_date, COUNT(DISTINCT order_id) AS order_count,
       SUM(order_total) AS gross_order_value
FROM retail_orders_curated
WHERE status IN ('PAID','SHIPPED')
GROUP BY order_date ORDER BY order_date;
