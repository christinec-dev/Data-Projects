-- Check missing data
SELECT
    SUM(hotel IS NULL) AS hotel_nulls,
    SUM(is_canceled IS NULL) AS is_canceled_nulls,
    SUM(lead_time IS NULL) AS lead_time_nulls,
    SUM(arrival_date_year IS NULL) AS arrival_date_year_nulls,
    SUM(arrival_date_month IS NULL) AS arrival_date_month_nulls,
    SUM(arrival_date_week_number IS NULL) AS arrival_date_week_number_nulls,
    SUM(arrival_date_day_of_month IS NULL) AS arrival_date_day_of_month_nulls,
    SUM(stays_in_weekend_nights IS NULL) AS stays_in_weekend_nights_nulls,
    SUM(stays_in_week_nights IS NULL) AS stays_in_week_nights_nulls,
    SUM(adults IS NULL) AS adults_nulls,
    SUM(children IS NULL) AS children_nulls,
    SUM(babies IS NULL) AS babies_nulls,
    SUM(meal IS NULL) AS meal_nulls,
    SUM(country IS NULL) AS country_nulls,
    SUM(market_segment IS NULL) AS market_segment_nulls,
    SUM(distribution_channel IS NULL) AS distribution_channel_nulls,
    SUM(is_repeated_guest IS NULL) AS is_repeated_guest_nulls,
    SUM(previous_cancellations IS NULL) AS previous_cancellations_nulls,
    SUM(previous_bookings_not_canceled IS NULL) AS previous_bookings_not_canceled_nulls,
    SUM(reserved_room_type IS NULL) AS reserved_room_type_nulls,
    SUM(assigned_room_type IS NULL) AS assigned_room_type_nulls,
    SUM(booking_changes IS NULL) AS booking_changes_nulls,
    SUM(deposit_type IS NULL) AS deposit_type_nulls,
    SUM(agent IS NULL) AS agent_nulls,
    SUM(company IS NULL) AS company_nulls,
    SUM(days_in_waiting_list IS NULL) AS days_in_waiting_list_nulls,
    SUM(customer_type IS NULL) AS customer_type_nulls,
    SUM(adr IS NULL) AS adr_nulls,
    SUM(required_car_parking_spaces IS NULL) AS required_car_parking_spaces_nulls,
    SUM(total_of_special_requests IS NULL) AS total_of_special_requests_nulls,
    SUM(reservation_status IS NULL) AS reservation_status_nulls,
    SUM(reservation_status_date IS NULL) AS reservation_status_date_nulls
FROM bookings;

-- children has 4 null values
-- Replace default value 0, for no children
SELECT * FROM bookings WHERE children IS NULL;
SELECT DISTINCT children FROM bookings;
UPDATE bookings
SET children = 0 WHERE children IS NULL;

-- country has 488 null values
-- Replace default value 'Other', for undefined
SELECT * FROM bookings WHERE country IS NULL;
SELECT DISTINCT country FROM bookings;
UPDATE bookings
SET country = 'Other' WHERE country IS NULL;

-- agent has 16340 null values
-- Drop column as it is only the agent ID who made booking
ALTER TABLE bookings
DROP COLUMN agent;

-- company has 112593 null values
-- Drop column as it is only the ID of the company/entity that made the booking
ALTER TABLE bookings
DROP COLUMN company;

-- The column previous_bookings_not_canceled is redundant, as previous_cancellations infer the same information
-- Drop it
ALTER TABLE bookings
DROP COLUMN previous_bookings_not_canceled;

-- Rename for better identification
ALTER TABLE bookings
RENAME COLUMN adr to avg_daily_rate,
RENAME COLUMN is_canceled to is_cancelled;

UPDATE bookings
SET customer_type = 'Individual' WHERE customer_type = 'Transient';
UPDATE bookings
SET customer_type = 'Individual-Party' WHERE customer_type = 'Transient-Party';
UPDATE bookings
SET customer_type = 'Business' WHERE customer_type = 'Contract';

-- View updated table
SELECT * FROM bookings LIMIT 10;
