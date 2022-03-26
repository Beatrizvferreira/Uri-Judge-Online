SELECT B.ID, 
       B.name
FROM categories as a
INNER JOIN products AS B ON (A.ID = B.id_categories)
WHERE A.NAME ~ 'super'