A1: SELECT SUM(COST) FROM PETRESCUE
A2: SELECT SUM(COST) AS SUM_OF_COST FROM PETRESCUE
A3: SELECT MAX(QUANTITY) FROM PETRESCUE
A4: SELECT AVG(COST) FROM PETRESCUE
A5: SELECT AVG(COST/QUANTITY) FROM PETRESCUE WHERE ANIMAL = 'Dog'

B1: SELECT ROUND(COST) FROM PETRESCUE
B2: SELECT LENGTH(ANIMAL) FROM PETRESCUE
B3: SELECT UCASE(ANIMAL) FROM PETRESCUE
B4: SELECT DISTINCT(UCASE(ANIMAL)) FROM PETRESCUE
B5: SELECT * FROM PETRESCUE WHERE LCASE(ANIMAL) = 'cat'

C1: SELECT DAY(RESCUEDATE) FROM PETRESCUE WHERE ANIMAL = 'cat'
C2: SELECT QUANTITY FROM PETRESCUE WHERE MONTH(RESCUEDATE) = '05'
C3: SELECT QUANTITY FROM PETRESCUE WHERE DAY(RESCUEDATE) = '14'
C4: SELECT DATE_add(RESCUEDATE, INTERVAL 3 DAY) from PETRESCUE
C5: SELECT DATEDIFF(CURRENT_TIMESTAMP,RESCUEDATE) from PETRESCUE

