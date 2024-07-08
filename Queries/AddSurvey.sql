ALTER PROCEDURE AddSurvey
@option varchar(50)
AS
UPDATE Survey
set vote_count+=1
WHERE options=@option