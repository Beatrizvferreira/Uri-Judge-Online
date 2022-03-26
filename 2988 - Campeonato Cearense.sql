SELECT NAME,
	SUM(CASE WHEN B.ID = A.TEAM_1 THEN 1
        WHEN B.ID = A.TEAM_2 THEN 1 ELSE 0 END) AS MATCHES,
    SUM(CASE WHEN A.team_1_goals < A.team_2_goals AND 
        A.TEAM_2 = B.ID THEN 1 
        WHEN A.team_2_goals < A.team_1_goals AND 
        A.TEAM_1 = B.ID THEN 1 ELSE 0 END) AS VICTORIES,
    SUM(CASE WHEN A.team_1_goals < A.team_2_goals AND 
        A.TEAM_1 = B.ID THEN 1
        WHEN A.team_2_goals < A.team_1_goals AND 
        A.TEAM_2 = B.ID THEN 1 ELSE 0 END) AS DEFEATS,
    SUM(CASE WHEN A.team_1_goals = A.team_2_goals AND 
        (A.TEAM_1 = B.ID OR A.TEAM_2 = B.ID) THEN 1 ELSE 0 END) AS DRAWS,
    SUM(CASE WHEN A.team_1_goals < A.team_2_goals AND 
        A.TEAM_2 = B.ID THEN 1 
        WHEN A.team_2_goals < A.team_1_goals AND 
        A.TEAM_1 = B.ID THEN 1 ELSE 0 END)*3 + SUM(CASE WHEN A.team_1_goals = A.team_2_goals AND 
        (A.TEAM_1 = B.ID OR A.TEAM_2 = B.ID) THEN 1 ELSE 0 END) AS SCORE
FROM matches A
INNER JOIN  teams B ON (A.team_1 = B.ID OR A.team_2 = B.ID)
GROUP BY NAME
ORDER BY SCORE DESC