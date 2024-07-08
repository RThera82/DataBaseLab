CREATE PROCEDURE SignUp
@firstname1 varchar(50),
@lastname1 varchar(50),
@password1 varchar(50),
@birth_date date,
@phone_number varchar(20),
@email varchar(max)
AS
INSERT INTO Users(first_name,last_name,password,birth_date,phone_number,email)
VALUES (@firstname1,@lastname1,@password1,@birth_date,@phone_number,@email)
