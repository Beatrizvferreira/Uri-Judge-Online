SELECT B.ID,
       B.NAME
FROM genres AS A 
INNER JOIN movies AS B ON (A.ID = B.id_genres)
WHERE A.description = 'Action'