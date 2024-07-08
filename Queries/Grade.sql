alter PROCEDURE Grades
@username varchar(50)
AS
SELECT DataBase1.score AS Database_score,DataStructure.score as Datastructure_score
FROM DataBase1 inner join Users 
on DataBase1.student_id=USERs.username
inner join DataStructure
on Users.username=DataStructure.student_id