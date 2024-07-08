ALTER PROCEDURE Login2
@username2 int,
@password2 varchar(50),
@IsSuccessful BIT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    SELECT *
    FROM Users
    WHERE username = @username2 AND  Users.password= @password2;

    IF @@ROWCOUNT > 0
    BEGIN
        SET @IsSuccessful = 1;
		PRINT 'SHOD'
    END
    ELSE
    BEGIN
        SET @IsSuccessful = 0;
    END
END;