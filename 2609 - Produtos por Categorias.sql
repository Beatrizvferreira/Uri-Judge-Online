
SELECT A.name,
       SUM(B.amount)
FROM categories AS a 
INNER JOIN products AS B ON (A.ID = B.id_categories)
GROUP BY  B.id_categories, A.name
