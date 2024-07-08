CREATE TRIGGER checkcapacity
ON DataStructure
AFTER INSERT
AS
DECLARE @row_count int;
SELECT row_count=COUNT(*) FROM DataStructure
IF @row_count>30 
	begin
	print 'The class is full!'
	rollback
	end