CREATE PROCEDURE enterScore
	@student_id INT,@score INT
	AS
		UPDATE DataStructure
		SET score=@score
		where student_id=student_id