create table Nutrition (
    nutr_id int primary key,
    item text not null,
    calories int not null,
    fat decimal not null,
    carb int not null,
    fiber int not null,
    protein int not null,
    nutr_type text not null,
    unique(nutr_id, item)
);