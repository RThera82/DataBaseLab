CREATE TABLE Users(
	first_name varchar(50) not null ,
	last_name varchar(50) not null,
	username INT not null IDENTITY(400213001,1),
	password varchar(50) not null,
	birth_date date,
	phone_number varchar(20),
	email varchar(max),
	Autority int,
	PRIMARY KEY(username)
);