# Ex01 -  create a new table called customers that contains all the data from the 4 tables created in the previous exercises

CREATE TABLE customers AS
SELECT * FROM data_2022_dec
UNION ALL
SELECT * FROM data_2022_nov
UNION ALL
SELECT * FROM data_2022_oct
UNION ALL
SELECT * FROM data_2023_jan
ORDER BY event_time;

DROP TABLE data_202*;
*can drop the original tables if you don't need them anymore*