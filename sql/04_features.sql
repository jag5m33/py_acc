
-- 4. removing impossible / erronous values 
-- check first: A count far larger than expected means the LIMIT is wrong, not the data.
SELECT
    COUNT(*) FILTER (WHERE "temperature(f)" NOT BETWEEN -70 AND 134) AS bad_temperature,
    COUNT(*) FILTER (WHERE "humidity(%)"    > 100) AS bad_humidity,
    COUNT(*) FILTER (WHERE "pressure(in)"   < 20) AS bad_pressure,
    COUNT(*) FILTER (WHERE "wind_speed(mph)" > 150) AS bad_wind_speed,
    COUNT(*) FILTER (WHERE start_lat NOT BETWEEN 20 AND 72) AS bad_lat,
    COUNT(*) FILTER (WHERE start_lng NOT BETWEEN -180 AND -60) AS bad_lng,
    COUNT(*) FILTER (WHERE "wind_chill(f)" > "temperature(f)") AS chill_above_temp
FROM source_2_dedup_cleaned;

-- get result:
CREATE OR REPLACE TABLE source_2_valid AS
SELECT * REPLACE (
    CASE WHEN "temperature(f)" NOT BETWEEN -70 AND 134
         THEN NULL ELSE "temperature(f)" END AS "temperature(f)",

    CASE WHEN "humidity(%)" > 100
         THEN NULL ELSE "humidity(%)" END AS "humidity(%)",

    CASE WHEN "pressure(in)" < 20
         THEN NULL ELSE "pressure(in)" END AS "pressure(in)",

    CASE WHEN "wind_speed(mph)" > 150
         THEN NULL ELSE "wind_speed(mph)" END AS "wind_speed(mph)",

    CASE WHEN start_lat NOT BETWEEN 20 AND 72
         THEN NULL ELSE start_lat END AS start_lat,

    CASE WHEN start_lng NOT BETWEEN -180 AND -60
         THEN NULL ELSE start_lng END AS start_lng
)
FROM source_2_dedup_cleaned;

SELECT COUNT(*) AS rows_after FROM source_2_valid;

