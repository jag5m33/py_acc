DESCRIBE source_2;
-- 1. Check ID is unique
SELECT COUNT(*) FROM source_2 GROUP BY id;

-- 2. Count Duplicate rows excluding id and the derived columns — expect ~3,581 in Source2
WITH d AS (
    SELECT * EXCLUDE (index, id) 
    FROM source_2
),
dup_groups AS (
    SELECT *, COUNT(*) AS n
    FROM d
    GROUP BY ALL
    HAVING COUNT(*) > 1
)
SELECT 
    COUNT(*) AS duplicate_groups,
    SUM(n) AS rows_in_groups,
    SUM(n) - COUNT(*) AS extra_copies 
    FROM dup_groups;
-- 3,581


    -- remove duplicates 
CREATE OR REPLACE TABLE source_2_dedup AS
SELECT 
    MIN(index) as index,  -- 3. aggregate the indexes to the first one out of all copies = carries one value through from each group
    MIN(id) as id, -- 3. aggeregates all ids to the first out of all copies = carries one value through from each group
    * EXCLUDE(index, id) -- 0. get all rows except index and id

FROM source_2
GROUP BY ALL; -- 1. groups all rows except index and id

SELECT COUNT(*) AS dedup_rows FROM source_2_dedup; -- correct number of rows left

-- 3. Dropping columns which are leaking data 
CREATE TABLE source_2_dedup_cleaned AS 
SELECT * EXCLUDE (
    end_time, 
    time_delta, 
    end_lat, 
    end_lng, 
    "distance(mi)", 
    source, 
    index, 
    bump, 
    give_way, 
    roundabout
) 
FROM source_2_dedup;
