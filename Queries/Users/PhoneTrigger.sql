CREATE TRIGGER phone_check
ON Users
AFTER INSERT,UPDATE
AS
SET NOCOUNT ON
IF NOT EXISTS(
	SELECT * 
	FROM inserted
	where LEN(inserted.phone_number)=11 and inserted.phone_number LIKE '09%'
)
BEGIN 
PRINT 'Invalid phone number!'
ROLLBACK
END