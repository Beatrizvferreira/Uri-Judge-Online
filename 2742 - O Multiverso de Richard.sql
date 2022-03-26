 SELECT B.NAME,
 	round(B.OMEGA*1.618,3) AS "Fator N" 
 FROM dimensions AS A
 INNER JOIN life_registry AS B ON (A.ID = B.dimensions_id)
 WHERE (A.NAME = 'C774' OR A.NAME = 'C875') AND  SUBSTR(B.NAME,1,7) = 'Richard'
        