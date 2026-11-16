-- since source 2 is the only sustainable source of information, extract frmom accidents 
-- 1. get column names to find out how to filter for source 2
SELECT * FROM accidents LIMIT 0; 

SELECT DISTINCT(source) FROM accidents;
-- 2. name of source 2 column: source 
CREATE TABLE source_2 AS
SELECT * FROM accidents WHERE source = 'Source2';

-- check that it is only source 2 = ~ 3m rows left 
SELECT COUNT(*) FROM source_2;
