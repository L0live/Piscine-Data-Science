# Exercise 2: Create a PostgreSQL table using the data from a CSV file

CREATE TABLE data_2022_dec(
    event_time TIMESTAMPTZ,
    event_type TEXT,
    product_id SERIAL,
    price REAL,
    user_id BIGSERIAL,
    user_session UUID
);

\copy data_2022_dec(event_time, event_type, product_id, price, user_id, user_session) FROM '/data_2022_dec.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');