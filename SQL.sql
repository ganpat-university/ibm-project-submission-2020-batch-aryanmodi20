CREATE TABLE proj_data(
	user_id INT,
	Yearly_avg_view_on_travel_page INT,
	frequentflyer INT,
	preferred_device VARCHAR(20),
	total_likes_on_outstation_checkin_given INT,
	yearly_avg_Outstation_checkins INT,
	annual_incom_class VARCHAR(5),
	member_in_family INT,
	booking_hotal  VARCHAR(5),
	preferred_location_type VARCHAR(20),
	working_flag INT,
	travelling_rating INT
);

SELECT * FROM proj_data


TRUNCATE TABLE proj_data

DECLARE @counter_tr INT = 100001

WHILE @counter_tr <= 110000
BEGIN
    DECLARE @user_id INT = @counter_tr
    DECLARE @Yearly_avg_view_on_travel_page INT = ABS(CHECKSUM(NEWID())) % 100 + 1
    DECLARE @frequentflyer INT = ABS(CHECKSUM(NEWID())) % 2
    DECLARE @preferred_device VARCHAR(20) = CASE WHEN ABS(CHECKSUM(NEWID())) % 2 = 0 THEN 'Mobile' ELSE 'Desktop' END
    DECLARE @total_likes_on_outstation_checkin_given INT = ABS(CHECKSUM(NEWID())) % 1000
    DECLARE @yearly_avg_Outstation_checkins INT = ABS(CHECKSUM(NEWID())) % 16  -- Change to 16 to limit it to 0-15
    DECLARE @annual_incom_class VARCHAR(5) = 
        CASE 
            WHEN ABS(CHECKSUM(NEWID())) % 3 = 0 THEN 'High' 
            WHEN ABS(CHECKSUM(NEWID())) % 3 = 1 THEN 'Low' 
            ELSE 'Average' 
        END
    DECLARE @member_in_family INT = ABS(CHECKSUM(NEWID())) % 5 + 1
    DECLARE @booking_hotal VARCHAR(5) = CASE WHEN ABS(CHECKSUM(NEWID())) % 2 = 0 THEN 'Yes' ELSE 'No' END
    DECLARE @preferred_location_type VARCHAR(20) = 
        CASE 
            WHEN ABS(CHECKSUM(NEWID())) % 8 = 0 THEN 'Big Cities'
            WHEN ABS(CHECKSUM(NEWID())) % 8 = 1 THEN 'Hill Station'
            WHEN ABS(CHECKSUM(NEWID())) % 8 = 2 THEN 'Trekking'
            WHEN ABS(CHECKSUM(NEWID())) % 8 = 3 THEN 'Historical Site'
            WHEN ABS(CHECKSUM(NEWID())) % 8 = 4 THEN 'Beach'
            WHEN ABS(CHECKSUM(NEWID())) % 8 = 5 THEN 'Islands'
            WHEN ABS(CHECKSUM(NEWID())) % 8 = 6 THEN 'Tech Cities'
            ELSE 'OTHER'
        END
    DECLARE @working_flag INT = CASE WHEN ABS(CHECKSUM(NEWID())) % 100 < 5 THEN 0 ELSE 1 END  -- Set working_flag for 5% of records
    DECLARE @travelling_rating INT = ABS(CHECKSUM(NEWID())) % 5 + 1

    INSERT INTO proj_data (
        user_id,
        Yearly_avg_view_on_travel_page,
        frequentflyer,
        preferred_device,
        total_likes_on_outstation_checkin_given,
        yearly_avg_Outstation_checkins,
        annual_incom_class,
        member_in_family,
        booking_hotal,
        preferred_location_type,
        working_flag,
        travelling_rating
    )
    VALUES (
        @user_id,
        @Yearly_avg_view_on_travel_page,
        @frequentflyer,
        @preferred_device,
        @total_likes_on_outstation_checkin_given,
        @yearly_avg_Outstation_checkins,
        @annual_incom_class,
        @member_in_family,
        @booking_hotal,
        @preferred_location_type,
        @working_flag,
        @travelling_rating
    )

    SET @counter_tr = @counter_tr + 1
END
