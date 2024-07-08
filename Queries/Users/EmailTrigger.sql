CREATE TRIGGER email_check
ON Users
AFTER INSERT,UPDATE
AS
	SET NOCOUNT ON
	IF EXISTS(
		SELECT * FROM inserted
		where inserted.email NOT LIKE '%@gmail.com'
	)
	BEGIN 
	PRINT 'Invalid email'
	ROLLBACK
	END