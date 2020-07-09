-- mondays.csv

SELECT 
	UNIX_TIMESTAMP(DATE(fecha)) as `day`, SUM(intensidad) 
FROM trafic 
WHERE WEEKDAY(fecha) = '0' 
GROUP BY day 
ORDER BY day 

INTO OUTFILE '/var/lib/mysql-files/mondays.csv' 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n';

-- byday.csv

select UNIX_TIMESTAMP(DATE(fecha)) as `day`, SUM(intensidad) from trafic GROUP BY day ORDER BY day INTO OUTFILE '/var/lib/mysql-files/byday.csv' FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
