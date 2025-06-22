-- Export final data via commands since file is big
SELECT 'reviewer_id','state','city','street','latitude','longitude','rating_count','review_time','review_date','days_since_review','rating_num'
UNION ALL
SELECT
       reviewer_id, state, city, street, latitude, longitude, rating_count, review_time, review_date, days_since_review, rating_num
FROM   reviews
INTO OUTFILE 'C:\\ProgramData\\MySQL\\MySQL Server 9.3\\Uploads\\reviews_cleaned.csv'
FIELDS TERMINATED BY ','  OPTIONALLY ENCLOSED BY '"'
LINES  TERMINATED BY '\n';

Select * from reviews;
