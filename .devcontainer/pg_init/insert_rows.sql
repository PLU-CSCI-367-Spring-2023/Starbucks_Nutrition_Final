copy nutrition(nutr_id, item, calories, fat, carb, fiber, protein, nutr_type)
from '/docker-entrypoint-initdb.d/seed_data/starbucks.csv'
delimiter ','
csv header;
