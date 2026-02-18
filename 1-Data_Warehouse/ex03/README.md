# Ex03 -  add the category_id, category_code and brand columns to the customers table and populate them with the corresponding values from the item table

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
*can drop the original item table if you don't need it anymore*