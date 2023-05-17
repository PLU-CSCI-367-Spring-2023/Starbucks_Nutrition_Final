copy nutrition(id, item, calories, fat, carb, fiber, protein, type)
from '/docker-entrypoint-initdb.d/seed_data/starbucks.csv'
delimiter ','
csv header;