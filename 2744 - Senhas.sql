SELECT ID, 
       password,
       MD5(PASSWORD) AS MD5
FROM account