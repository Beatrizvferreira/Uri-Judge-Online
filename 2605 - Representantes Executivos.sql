 SELECT B.NAME,
             C.NAME 
      FROM CATEGORIES AS A
      INNER JOIN PRODUCTS AS B 
              ON B.id_categories = A.ID
      INNER JOIN PROVIDERS AS c 
              ON B.id_providers = C.ID
      WHERE A.ID = 6;