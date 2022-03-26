SELECT A.NAME,
	   ROUND(SUM((B.hours*150)+((B.hours*150)*C.BONUS/100)),1) AS SALARY
FROM doctors A 
INNER JOIN attendances B ON (A.ID = B.ID_DOCTOR)
INNER JOIN work_shifts C ON (C.ID = B.id_work_shift)
group by a.name
ORDER BY 2 DESC