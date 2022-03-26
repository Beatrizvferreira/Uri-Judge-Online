SELECT A.ID,
       B.ID
FROM providers A 
LEFT join products B ON (A.ID = B.id_customers);