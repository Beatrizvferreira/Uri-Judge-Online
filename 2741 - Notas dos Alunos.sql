SELECT CONCAT('Approved: ', NAME) AS NAME,
       GRADE
FROM students
WHERE grade>=7
ORDER BY 2 DESC