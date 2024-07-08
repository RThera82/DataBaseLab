CREATE TABLE Letter(
	code int PRIMARY KEY IDENTITY(100,1),
	datel datetime,
	sender int,
	title varchar(max),
	body varchar(max)
);