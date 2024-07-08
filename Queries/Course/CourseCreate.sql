CREATE TABLE Course(
	Cname varchar(20) NOT NULL,
	Code int IDENTITY(1000,1) NOT NULL,
	professor_name varchar(50) NOT NULL,
	capacity int NOT NULL,
	credit int NOT NULL,
	Ctime varchar(max) NOT NULL,
	Clocation varchar(50) NOT NULL
	PRIMARY KEY(Code)
);