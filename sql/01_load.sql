CREATE TABLE accidents AS
SELECT * FROM read_parquet('data/df_temp.parquet');

-- check that the file is correct in number of rows 
SELECT COUNT(*) FROM accidents;



