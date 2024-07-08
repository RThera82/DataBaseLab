CREATE PROCEDURE enterGrade
@student_id int,
@grade2 int
AS
UPDATE DataStructure
SET score=@grade2
where student_id=@grade2