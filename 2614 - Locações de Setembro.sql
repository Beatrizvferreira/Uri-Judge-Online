SELECT B.NAME, 
       A.RENTALS_DATE
FROM rentals AS A
INNER JOIN customers AS B ON (A.id_customers = B.id)
WHERE extract('month' from A.rentals_date)=9