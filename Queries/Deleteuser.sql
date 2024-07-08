CREATE PROCEDURE DeleteAccount
@username3 int,
@password3 varchar(50),
@IsDeleted3 BIT OUTPUT
AS 
SET NOCOUNT ON;
IF EXISTS(
	SELECT 1 FROM  Users WHERE
	username=@username3 and Users.password=@password3
)
BEGIN
	DELETE FROM Users 
	WHERE
	username=@username3 and Users.password=@password3
	SET @IsDeleted3=1
	END
	ELSE
	begin 
	SET @IsDeleted3=0
	END