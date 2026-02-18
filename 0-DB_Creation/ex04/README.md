# Ex04 -  create a table for the item.csv file and copy the data into it

CREATE TABLE item(
    product_id SERIAL,
    category_id BIGINT,
    category_code TEXT,
    brand TEXT
);

\copy item(product_id, category_id, category_code, brand) FROM '/item.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');