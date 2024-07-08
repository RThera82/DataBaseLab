CREATE TRIGGER passwordcheck
ON Users 
AFTER INSERT,UPDATE
AS
SET NOCOUNT ON
IF EXISTS(
	SELECT inserted.password
	FROM inserted
	WHERE password NOT LIKE '%[0-9]%' OR inserted.password NOT LIKE '%[!@#$%^&*(),.?":{}|<>]%' OR inserted.password NOT LIKE '%[A-Z]%'
)
BEGIN
PRINT('Your password should contain number,capitable charachter and special charachter')
ROLLBACK
END