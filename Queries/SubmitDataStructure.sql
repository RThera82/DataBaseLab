ALTER PROCEDURE submitdatastructure
@studentname varchar(50),
@studentlastname varchar(50),
@studentid int
AS
INSERT INTO DataStructure(student_name,student_lastname,student_id)
VALUES(@studentname,@studentlastname,@studentid)
IF @@ROWCOUNT=0
BEGIN
PRINT 'Failed!'
end
ELSE
begin
PRINT 'Successfull!'
END
