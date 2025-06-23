SELECT * FROM bookings
INTO OUTFILE 'C:\\ProgramData\\MySQL\\MySQL Server 9.3\\Uploads\\bookings_final.csv'
FIELDS TERMINATED BY ','  OPTIONALLY ENCLOSED BY '"'
LINES  TERMINATED BY '\n';