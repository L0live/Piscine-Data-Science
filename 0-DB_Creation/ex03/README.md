docker compose up

docker ps
-> get the container_id of the running PostgreSQL container

docker cp ./customer container_id:/customer

python3 script.py customer
docker cp ./import_data.sql container_id:/import_data.sql

docker exec -it container_name bash

psql -U your_login -d piscineds -h localhost -W < import_data.sql
-> type your password when prompted

^D

docker exec -it container_name pg_dump -U your_login -d piscineds -h localhost -W > automatic_table.sql
-> don't forget to type your password, the prompt is in the file