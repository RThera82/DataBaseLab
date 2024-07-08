CREATE PROCEDURE SendLetter
@sender int,
@title varchar(max),
@body varchar(max),
@isSent bit output
AS
INSERT INTO Letter(datel,sender,title,body)
VALUES(GETDATE(),@sender,@title,@body)
IF @@ROWCOUNT>0
BEGIN
set @isSent=1
end
else
begin
set @isSent=0
end