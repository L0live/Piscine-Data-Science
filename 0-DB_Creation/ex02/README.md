docker compose up

docker ps
-> get the container_id of the running PostgreSQL container

docker cp ./customer/data_2022_dec.csv container_id:/data_2022_dec.csv

docker exec -it container_name psql -U your_login -d piscineds -h localhost -W
-> type your password when prompted

CREATE TABLE data_2022_dec(
    event_time TIMESTAMPTZ,
    event_type TEXT,
    product_id SERIAL,
    price REAL,
    user_id BIGSERIAL,
    user_session UUID
);

\copy data_2022_dec(event_time, event_type, product_id, price, user_id, user_session) FROM '/data_2022_dec.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');

SELECT * FROM data_2022_dec LIMIT 10;
-> check if the data has been imported correctly

^D

docker exec -it container_name pg_dump -U your_login -d piscineds -h localhost -W > table.sql
-> don't forget to type your password, the prompt is in the file