-- View created table
SELECT * FROM reviews;

-- Drop store_name, since all the values are 'McDonald's'
-- Drop category, since all the values are 'Fast food restaurant'
ALTER TABLE reviews
	DROP COLUMN store_name,
	DROP COLUMN category;

-- Extract the number from rating
ALTER TABLE reviews
	ADD COLUMN rating_num INT AFTER rating;
    
UPDATE reviews
	SET rating_num = CAST(SUBSTRING_INDEX(rating, ' ' , 1) AS UNSIGNED);
    
ALTER TABLE reviews
	DROP COLUMN rating;

-- Change review time into actual date format
ALTER TABLE mcd_reviews.reviews
  ADD COLUMN review_date DATE NULL AFTER review_time,
  ADD COLUMN days_since_review INT NULL AFTER review_date;
  
SET @SCRAPE_DATE = '2025-06-01';
UPDATE mcd_reviews.reviews
SET
  days_since_review = CASE
      WHEN review_time RLIKE '^[0-9]+\\s+day'   THEN CAST(REGEXP_SUBSTR(review_time,'[0-9]+') AS UNSIGNED)
      WHEN review_time RLIKE '^a\\s+day'        THEN 1
      WHEN review_time RLIKE '^[0-9]+\\s+week'  THEN CAST(REGEXP_SUBSTR(review_time,'[0-9]+') AS UNSIGNED) * 7
      WHEN review_time RLIKE '^a\\s+week'       THEN 7
      WHEN review_time RLIKE '^[0-9]+\\s+month' THEN CAST(REGEXP_SUBSTR(review_time,'[0-9]+') AS UNSIGNED) * 30
      WHEN review_time RLIKE '^a\\s+month'      THEN 30
      WHEN review_time RLIKE '^[0-9]+\\s+year'  THEN CAST(REGEXP_SUBSTR(review_time,'[0-9]+') AS UNSIGNED) * 365
      WHEN review_time RLIKE '^a\\s+year'       THEN 365
  END,
  review_date = DATE_SUB(
	@SCRAPE_DATE,
    INTERVAL days_since_review DAY
);

-- Check for missing data
SELECT
    SUM(store_address IS NULL) AS store_address_nulls,
    SUM(longitude IS NULL) AS longitude_nulls,
    SUM(latitude IS NULL) AS latitude_nulls,
    SUM(rating_count IS NULL) AS rating_count_nulls,
    SUM(review_time IS NULL) AS review_time_nulls,
    SUM(rating_num IS NULL) AS rating_num_nulls
FROM reviews;

-- Both latitude and longitude have 660 missing values
SELECT * FROM reviews WHERE latitude IS NULL;
SELECT * FROM reviews WHERE longitude IS NULL;

-- All of these values come from the same address, which seems to be 2476 Kalakaua Ave, Waikiki
SELECT * FROM reviews WHERE store_address = '2476 Kalï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½';
UPDATE reviews
	SET 
		store_address = '2476 Kalakaua Ave, Honolulu, Oahu, HI 96815',
        latitude = 21.2746060049047,
        longitude = -157.824262202943
	WHERE store_address LIKE '2476 Kal%' AND rating_count = 2175;
    
-- Re-check for missing data
SELECT
    SUM(store_address IS NULL) AS store_address_nulls,
    SUM(longitude IS NULL) AS longitude_nulls,
    SUM(latitude IS NULL) AS latitude_nulls,
    SUM(rating_count IS NULL) AS rating_count_nulls,
    SUM(review_time IS NULL) AS review_time_nulls,
    SUM(rating_num IS NULL) AS rating_num_nulls
FROM reviews;

-- Split store_address to get City and State
ALTER TABLE reviews
	ADD COLUMN state VARCHAR(2) AFTER store_address,
	ADD COLUMN city VARCHAR(100) AFTER state,
	ADD COLUMN street VARCHAR(150) AFTER city;
    UPDATE reviews
    
SET
  /* chunk before the 1st comma --------------- */
  street = TRIM( SUBSTRING_INDEX(store_address, ',', 1) ),
  /* chunk between 1st and 2nd comma ---------- */
  city   = TRIM( SUBSTRING_INDEX(
                    SUBSTRING_INDEX(store_address, ',', 2), ',', -1) ),
  /* chunk between 2nd and 3rd comma ---------- */
  state  = SUBSTRING_INDEX(
             TRIM( SUBSTRING_INDEX(
                     SUBSTRING_INDEX(store_address, ',', 3), ',', -1) ),
             ' ', 1);

-- Drop column             
ALTER TABLE reviews
DROP COLUMN store_address;

-- Final table
SELECT * FROM reviews;