SELECT A.NAME,
       B.ID
FROM customers A
LEFT JOIN orders B ON (A.ID = B.id_customers)
WHERE B.orders_date > '2016-01-01' AND B.orders_date < '2016-06-30'