-- FINAL CLEANING STAGES:
-- columns that need to be removed for hte final modelling stages:
-- street, weather_condition, sunrise_sunset, civil_twilight, nautical_twilight, astronomical_twilight, start_time, weather_timestamp, airport_code, wind_chill(f), precipitation(in)
CREATE OR REPLACE TABLE source_2_final AS
SELECT * EXCLUDE (street, weather_condition, sunrise_sunset, civil_twilight,
                  nautical_twilight, astronomical_twilight, start_time,
                  weather_timestamp, airport_code, "wind_chill(f)", "precipitation(in)")
FROM source_2_weather
WHERE light_score IS NOT NULL;

SELECT COUNT(*) FROM source_2_final;