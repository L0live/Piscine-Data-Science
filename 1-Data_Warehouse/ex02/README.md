docker compose up

docker ps
-> get the container_id of the running PostgreSQL container

docker cp ./customers_table.sql container_id:/customers_table.sql

docker exec -it container_name bash

psql -U your_login -d piscineds -h localhost -W < customers_table.sql
-> type your password when prompted

psql -U your_login -d piscineds -h localhost -W
-> type your password when prompted

DELETE FROM customers a
USING customers b
WHERE a.ctid < b.ctid
AND a.event_type = b.event_type
AND a.product_id = b.product_id
AND a.price = b.price
AND a.user_id = b.user_id
AND a.user_session = b.user_session
AND ABS(EXTRACT(EPOCH FROM (a.event_time - b.event_time))) <= 1;

^D^D

docker exec -it container_name pg_dump -U your_login -d piscineds -h localhost -W > remove_duplicates.sql
-> don't forget to type your password, the prompt is in the file