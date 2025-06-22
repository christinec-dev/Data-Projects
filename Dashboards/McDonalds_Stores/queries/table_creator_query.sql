-- Create table with necessary columns
CREATE TABLE IF NOT EXISTS `mcd_reviews`.`reviews` (
  `reviewer_id` INT NULL,
  `store_name` VARCHAR(25) NULL,
  `category` VARCHAR(50) NULL,
  `store_address` VARCHAR(100) NULL,
  `latitude` DECIMAL(9,6) NULL,
  `longitude` DECIMAL(9,6) NULL,
  `rating_count` INT NULL,
  `review_time` VARCHAR(50) NULL,
  `rating` VARCHAR(25) NULL
);

-- Load data into table
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 9.3\\Uploads\\reviews.csv'
INTO TABLE mcd_reviews.reviews
CHARACTER SET latin1              
FIELDS  TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        ESCAPED BY '"'          
LINES   TERMINATED BY '\r\n'
IGNORE 1 LINES
(
  reviewer_id,                     -- 1
  store_name,                      -- 2
  category,                        -- 3
  store_address,                   -- 4
  @lat,                            -- 5
  @long,                           -- 6
  @rating_cnt,                     -- 7
  review_time,                     -- 8
  @dummy,                          -- 9  ← skipped review since it contains paragraphs
  rating                           -- 10
)
SET
  latitude     = NULLIF(@lat,''),
  longitude    = NULLIF(@long,''),
  rating_count = NULLIF(@rating_cnt,'');

-- View created table
SELECT * FROM reviews;

-- Commit
COMMIT;
