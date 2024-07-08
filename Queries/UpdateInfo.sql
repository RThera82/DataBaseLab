ALTER PROCEDURE UpdataInfo
@user int,
@phone varchar(20),
@birth2 date,
@emailU varchar(max)
AS
UPDATE Users
SET birth_date=@birth2,phone_number=@phone,email=@emailU
where username=@user