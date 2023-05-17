create table Nutrition (
    id int primary key,
    item text not null,
    calories int not null,
    fat decimal not null,
    carb int not null,
    fiber int not null,
    protein int not null,
    type text not null,
    unique(id, item)
);