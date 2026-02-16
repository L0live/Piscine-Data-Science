docker compose up

docker ps
-> get the container_id of the running PostgreSQL container

docker cp ./remove_duplicates.sql container_id:/remove_duplicates.sql
docker cp ./items_table.sql container_id:/items_table.sql

docker exec -it container_name bash

psql -U your_login -d piscineds -h localhost -W < remove_duplicates.sql
-> type your password when prompted

psql -U your_login -d piscineds -h localhost -W < items_table.sql
-> type your password when prompted

psql -U your_login -d piscineds -h localhost -W
-> type your password when prompted

ALTER TABLE customers
ADD COLUMN category_id BIGINT,
ADD COLUMN category_code TEXT,
ADD COLUMN brand TEXT;

UPDATE customers c
SET category_id = i.category_id,
    category_code = i.category_code,
    brand = i.brand
FROM item i
WHERE c.product_id = i.product_id;

DROP TABLE item;
-> can drop the original item table if you don't need it anymore

^D^D

docker exec -it container_name pg_dump -U your_login -d piscineds -h localhost -W > fusion.sql
-> don't forget to type your password, the prompt is in the file