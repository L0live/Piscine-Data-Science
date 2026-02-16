docker compose up

docker ps
-> get the container_id of the running PostgreSQL container

docker cp ./item/item.csv container_id:/item.csv

docker exec -it container_name psql -U your_login -d piscineds -h localhost -W
-> type your password when prompted

CREATE TABLE item(
    product_id SERIAL,
    category_id BIGINT,
    category_code TEXT,
    brand TEXT
);

\copy item(product_id, category_id, category_code, brand) FROM '/item.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');

SELECT * FROM item LIMIT 10;
-> check if the data has been imported correctly

^D

docker exec -it container_name pg_dump -U your_login -d piscineds -h localhost -W > items_table.sql
-> don't forget to type your password, the prompt is in the file