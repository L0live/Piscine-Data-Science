docker compose up

docker ps
-> get the container_id of the running PostgreSQL container

docker cp ./automatic_table.sql container_id:/automatic_table.sql

docker exec -it container_name bash

psql -U your_login -d piscineds -h localhost -W < automatic_table.sql
-> type your password when prompted

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
-> can drop the original tables if you don't need them anymore

^D^D

docker exec -it container_name pg_dump -U your_login -d piscineds -h localhost -W > customers_table.sql
-> don't forget to type your password, the prompt is in the file