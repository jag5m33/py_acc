-- 5a. 
-- CASE WHEN IN/NOT/BETWEEN/=/>/< THEN ELSE END AS - end as = gives the resulting column alias (resulting col. name)
CREATE OR REPLACE TABLE source_2_features AS
SELECT
    *,
    CASE WHEN severity IN (3,4) THEN 1 ELSE 0 END AS severe,
    CASE WHEN light_score = 4  THEN 1 ELSE 0 END AS is_night,

    CAST(traffic_signal AS INT)
      + CAST(crossing AS INT)
      + CAST(stop AS INT)
      + CAST(amenity AS INT)
      + CAST(station AS INT) AS constraint_count,

    EXTRACT(year   FROM start_time)     AS start_year,
    EXTRACT(hour   FROM start_time)     AS start_hour,
    EXTRACT(isodow FROM start_time) - 1 AS start_day
FROM source_2_valid;

SELECT COUNT(*) AS rows, AVG(severe)*100 AS pct_severe FROM source_2_features;

--5b. Trim, lower case weather_condition & put into groups: 
-- is_rain, is_snow, is_ice, is_thunder, is_fog, is_obscured, is_windy, weather_missing
CREATE OR REPLACE TABLE source_2_weather AS
SELECT
    *,
    CASE WHEN regexp_matches(LOWER(TRIM(weather_condition)), 'rain|drizzle|shower')
         THEN 1 ELSE 0 END AS is_rain,

    CASE WHEN regexp_matches(LOWER(TRIM(weather_condition)), 'snow|wintry|flurr')
         THEN 1 ELSE 0 END AS is_snow,

    CASE WHEN regexp_matches(LOWER(TRIM(weather_condition)), 'ice|icy|sleet|hail|freezing|pellet')
         THEN 1 ELSE 0 END AS is_ice,

    CASE WHEN regexp_matches(LOWER(TRIM(weather_condition)), 'thunder|t-storm|tstorm|squall|tornado|funnel')
         THEN 1 ELSE 0 END AS is_thunder,

    CASE WHEN regexp_matches(LOWER(TRIM(weather_condition)), 'fog|mist')
         THEN 1 ELSE 0 END AS is_fog,

    CASE WHEN regexp_matches(LOWER(TRIM(weather_condition)), 'haze|smoke|dust|sand|ash')
         THEN 1 ELSE 0 END AS is_obscured,

    CASE WHEN regexp_matches(LOWER(TRIM(weather_condition)), 'windy|blowing|drifting|whirl')
         THEN 1 ELSE 0 END AS is_windy,

    CASE WHEN weather_condition IS NULL
           OR LOWER(TRIM(weather_condition)) = 'n/a precipitation'
         THEN 1 ELSE 0 END AS weather_missing
FROM source_2_features;

-- Check against the Python counts
SELECT
    SUM(is_rain) AS is_rain, -- target 244,933
    SUM(is_snow) AS is_snow, -- target  54,314
    SUM(is_fog) AS is_fog, -- target  44,463
    SUM(is_obscured) AS is_obscured, -- target  38,543
    SUM(is_thunder) AS is_thunder, -- target  34,407
    SUM(is_windy) AS is_windy, -- target  27,458
    SUM(is_ice) AS is_ice, -- target   3,501
    SUM(weather_missing) AS weather_missing -- ~63,490
FROM source_2_weather;

--5c. intensity groupings : frmo 0,1,2
CREATE OR REPLACE TABLE source_2_weather AS
SELECT *, CASE
    WHEN is_rain + is_snow + is_ice + is_thunder
       + is_fog + is_obscured + is_windy = 0 THEN NULL
    WHEN regexp_matches(LOWER(TRIM(weather_condition)), 'light|shallow|patches') THEN 0
    WHEN regexp_matches(LOWER(TRIM(weather_condition)), 'heavy') THEN 2 ELSE 1
    END AS intensity
FROM source_2_weather;

-- check with positional reference, group by intensity (1) and order by intensity (1)
SELECT intensity, COUNT(*) FROM source_2_weather GROUP BY 1 ORDER BY 1;

-- 5d. Check the street type categorisation:
SELECT street_type, COUNT(*) as street_type_counts FROM source_2_weather GROUP BY 1, ORDER BY 2;
