SELECT A.NAME
FROM customers A 
RIGHT JOIN legal_person B ON (A.ID = B.id_customers)