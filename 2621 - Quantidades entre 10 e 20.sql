SELECT B.NAME
FROM providers A 
INNER JOIN products B ON (A.ID = B.id_providers)
WHERE B.amount >=10 AND B.amount <=20 AND SUBSTR(A.NAME,1,1) = 'P'