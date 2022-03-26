SELECT A.NAME, 
       B.NAME
FROM products A 
LEFT JOIN categories B ON (A.id_categories = B.ID)
WHERE AMOUNT > 100 AND (B.ID = 1 OR B.ID = 2 OR B.ID = 3 OR B.ID=6 OR B.ID=9)
ORDER BY B.ID