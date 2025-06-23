-- Create table
CREATE TABLE IF NOT EXISTS `hotel_bookings`.`bookings` (
  `booking_id` INT AUTO_INCREMENT,
  `hotel` VARCHAR(100) NULL,
  `is_canceled` INT NULL,
  `lead_time` INT NULL,
  `arrival_date_year` INT NULL,
  `arrival_date_month` VARCHAR(20) NULL,
  `arrival_date_week_number` INT NULL,
  `arrival_date_day_of_month` INT NULL,
  `stays_in_weekend_nights` INT NULL,
  `stays_in_week_nights` INT NULL,
  `adults` INT NULL,
  `children` INT NULL,
  `babies` INT NULL,
  `meal` VARCHAR(100) NULL,
  `country` VARCHAR(100) NULL,
  `market_segment` VARCHAR(100) NULL,
  `distribution_channel` VARCHAR(100) NULL,
  `is_repeated_guest` INT NULL,
  `previous_cancellations` INT NULL,
  `previous_bookings_not_canceled` INT NULL,
  `reserved_room_type` VARCHAR(100) NULL,
  `assigned_room_type` VARCHAR(100) NULL,
  `booking_changes` INT NULL,
  `deposit_type` VARCHAR(100) NULL,
  `agent` DECIMAL(12,2) NULL,
  `company` DECIMAL(12,2) NULL,
  `days_in_waiting_list` INT NULL,
  `customer_type` VARCHAR(100) NULL,
  `adr` DECIMAL(12,2) NULL,
  `required_car_parking_spaces` INT NULL,
  `total_of_special_requests` INT NULL,
  `reservation_status` VARCHAR(100) NULL,
  `reservation_status_date` DATE NULL,
  PRIMARY KEY (booking_id)
);

-- Load data into `hotel_bookings`.`bookings`
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.3/Uploads/hotel_bookings_original.csv'
INTO TABLE `hotel_bookings`.`bookings`
CHARACTER SET ascii
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '\\'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(

  @hotel ,                         -- 1,
  @is_canceled        ,            -- 2,
  @lead_time       ,               -- 3,
  @arrival_date_year       ,       -- 4,
  @arrival_date_month         ,    -- 5,
  @arrival_date_week_number    ,   -- 6,
  @arrival_date_day_of_month    ,  -- 7,
  @stays_in_weekend_nights    ,    -- 8,
  @stays_in_week_nights     ,      -- 9,
  @adults                 ,        -- 10,
  @children             ,          -- 11,
  @babies              ,           -- 12,
  @meal               ,            -- 13,
  @country              ,          -- 14,
  @market_segment           ,      -- 15,
  @distribution_channel        ,   -- 16,
  @is_repeated_guest         ,     -- 17,
  @previous_cancellations     ,    -- 18,
  @previous_bookings_not_canceled ,-- 19,
  @reserved_room_type       ,      -- 20,
  @assigned_room_type     ,        -- 21,
  @booking_changes            ,    -- 22,
  @deposit_type              ,     -- 23,
  @agent                    ,      -- 24,
  @company                    ,    -- 25,
  @days_in_waiting_list        ,   -- 26,
  @customer_type               ,   -- 27,
  @adr                         ,   -- 28,
  @required_car_parking_spaces   , -- 29,
  @total_of_special_requests     , -- 30,
  @reservation_status         ,    -- 31,
  @reservation_status_date      -- 32
)
SET
  hotel                          = NULLIF(@hotel,''),
  is_canceled                    = NULLIF(@is_canceled,''),
  lead_time                      = NULLIF(@lead_time,''),
  arrival_date_year              = NULLIF(@arrival_date_year,''),
  arrival_date_month             = NULLIF(@arrival_date_month,''),
  arrival_date_week_number       = NULLIF(@arrival_date_week_number,''),
  arrival_date_day_of_month      = NULLIF(@arrival_date_day_of_month,''),
  stays_in_weekend_nights        = NULLIF(@stays_in_weekend_nights,''),
  stays_in_week_nights           = NULLIF(@stays_in_week_nights,''),
  adults   = IF(@adults   IN ('', 'NA', 'NULL'), NULL, @adults),
  children = IF(@children IN ('', 'NA', 'NULL'), NULL, @children),
  babies   = IF(@babies   IN ('', 'NA', 'NULL'), NULL, @babies),
  meal                           = NULLIF(@meal,''),
  country                        = NULLIF(@country,''),
  market_segment                 = NULLIF(@market_segment,''),
  distribution_channel           = NULLIF(@distribution_channel,''),
  is_repeated_guest              = NULLIF(@is_repeated_guest,''),
  previous_cancellations         = NULLIF(@previous_cancellations,''),
  previous_bookings_not_canceled = NULLIF(@previous_bookings_not_canceled,''),
  reserved_room_type             = NULLIF(@reserved_room_type,''),
  assigned_room_type             = NULLIF(@assigned_room_type,''),
  booking_changes                = NULLIF(@booking_changes,''),
  deposit_type                   = NULLIF(@deposit_type,''),
  agent                          = NULLIF(@agent,''),
  company                        = NULLIF(@company,''),
  days_in_waiting_list           = NULLIF(@days_in_waiting_list,''),
  customer_type                  = NULLIF(@customer_type,''),
  adr                            = NULLIF(@adr,''),
  required_car_parking_spaces    = NULLIF(@required_car_parking_spaces,''),
  total_of_special_requests      = NULLIF(@total_of_special_requests,''),
  reservation_status             = NULLIF(@reservation_status,''),
  reservation_status_date        = NULLIF(@reservation_status_date,'');

-- View table
SELECT * FROM bookings LIMIT 10;

-- Commit
Commit;