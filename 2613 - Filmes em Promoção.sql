SELECT B.ID,
       B.NAME
FROM prices AS A 
INNER JOIN movies AS B ON (A.ID = B.id_prices)
WHERE A.value < 2