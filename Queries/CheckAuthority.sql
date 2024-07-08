CREATE PROCEDURE CheckUserAuthority
    @username NVARCHAR(50),
    @CanEnterScore BIT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @authority INT;
    SELECT @authority = autority
    FROM Users
    WHERE username = @username;
    IF @authority = 1
    BEGIN
        SET @CanEnterScore = 1;
    END
    ELSE
    BEGIN
        SET @CanEnterScore = 0;
    END
END