SELECT A.ID,
       A.NAME
FROM customers A 
LEFT join locations B ON (A.ID = B.id_customers)
where B.id_customers IS NULL;