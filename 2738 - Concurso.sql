SELECT A.NAME,
      round(((B.MATH*2)+(B.SPECIFIC*3)+(B.PROJECT_PLAN*5))/10,2) AS AVG
FROM candidate A
LEFT JOIN score B ON (A.ID = B.candidate_id)
ORDER BY AVG DESC