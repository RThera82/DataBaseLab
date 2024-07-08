CREATE TRIGGER birth_check
ON Users
AFTER INSERT,UPDATE
AS
SET NOCOUNT ON
IF EXISTS(
	SELECT inserted.birth_date
	FROM inserted
	where DATEDIFF(year,inserted.birth_date,GETDATE())>100
)
BEGIN 
PRINT 'Invalid birth time!'
ROLLBACK
END