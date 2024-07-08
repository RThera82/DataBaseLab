import pyodbc

class ConsoleDataBase:
    def __init__(self):
        self.connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=SHR;'
                      'Database=Project;'
                      'Trusted_Connection=yes;')
        self.login=False
        self.login2=True

    def menu(self):
        print("Hello, which one of these do you want:")
        print("1-Sign up")
        print("2-Log in")

        choice = input("Enter your choice: ")

        if choice=='1':
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            phone = input("Enter your phone number: ")
            birthday = input("Enter your birthday: ")
            self.SignUp(first_name,last_name,password,birthday,phone,email)
            print("Sign Up successfully!")
        
        elif choice=='2':
            pass
            # username=int(input("Please enter your username:"))
            # password=input("Please enter your password:")
            # self.login=Login(username,password)
        else:
            print("Invalid choice")

        if(self.login2):
            print("1-Send letter")
            print("2-Submit in class")
            print("3-Update your information")
            print("4-Assign Survey")
            print("5-Delete Account")
            print("6-See Grades")
            print("7-Enter grade")
            opt=int(input("Welcome,what do you want to do?"))

            if opt==1:
                sender=input("Enter your student_id: ")
                tile=input("Enter the title of letter: ")
                body=input("Enter the body of letter: ")
                self.SendLetter(sender,tile,body)

            elif opt==2:
                print("1-Data structure")
                print("2-Data base")
                which=int(input("Which class do you want to submit?"))
                if (which==1):
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    student_id = int(input("Enter student ID: "))
                    self.submitDataStructure(first_name, last_name, student_id)
                elif which==2:
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    student_id = int(input("Enter student ID: "))
                    self.submitDataBase(first_name, last_name, student_id)
                else:
                    print("Invalid choice")

            elif opt==3:
                user=int(input("Enter your username: "))
                phone=input("Enter new phone number: ")
                email=input("Enter new your email: ")
                birthday=input("Enter new birth time: ")
                self.UpdateInfo(user,phone,birthday,email)

            elif opt==4:
                self.showSurvey()
                vote=input("Please enter the option that you want to vote")
                self.Addvote(opt)
            
            elif opt==5:
                username1=input("Enter your username: ")
                password1=input("Enter your password: ")
                self.DeleteAccount(username1,password1)
            
            elif opt==6:
                grade=int(input("Enter your username: "))
                self.SeeGrade(grade)
            
            elif opt==7:
                username=int(input("Enter your username: "))
                student_id=int(input("Enter student ID: "))
                score=int(input("Enter  score: "))
                self.enterGrade(username,student_id,score)


    def SignUp(self,first_name,last_name,password,birth_date,phone_number,email):
        try:
            cursor=self.connection.cursor()
            cursor.execute("{CALL SignUp (?, ?, ?,?,?,?)}",first_name,last_name,password,birth_date,phone_number,email)
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
    

    def Login(self,username,password):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                DECLARE @test BIT;
                EXEC Login2  ?, ?, @IsSuccessful = @test OUTPUT;
                SELECT @test;
            ''', (username,password))
            result=cursor.fetchone()
            if result!= None:
                print("Login successfully!")
                cursor.close()
                return True
            else:
                print("Login failed")
                cursor.close()
                return False
        except Exception as e:
            print(f"Error: {e}")


    def submitDataBase(self,first_name, last_name, student_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("{CALL submitdatabase (?, ?, ?)}", first_name, last_name, student_id)
            self.connection.commit()
            print("Data submitted successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()


    def DeleteAccount(self,username,password):
        cursor = self.connection.cursor()
        is_deleted=0
        cursor.execute("""
            DECLARE @test2 BIT;
            EXEC DeleteAccount ?, ?, @IsDeleted3 = ? OUTPUT
        """, (username, password,is_deleted))

        cursor.commit()
        cursor.close()
        if is_deleted == 0:
            print("User deleted successfully.")
        else:
            print("Failed to delete user .")



    def submitDataStructure(self,first_name, last_name, student_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("{CALL submitdatastructure (?, ?, ?)}", first_name, last_name, student_id)
            self.connection.commit()
            print("Data submitted successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()


    def SeeGrade(self,username):
        try:
            cursor = self.connection.cursor()
            cursor.execute("{CALL Grades (?)}", username)
            columns=[column[0] for column in cursor.description]
            print(columns)
            while True:
                row=cursor.fetchone()
                if not row:
                    break
                print(row)


        finally:
            cursor.close()


    def UpdateInfo(self,username,phone,birth,email):
        try:
            cursor = self.connection.cursor()
            cursor.execute("{CALL UpdataInfo (?, ?, ?,?)}", username, phone,birth,email)
            self.connection.commit()
            print("Data updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()


    def CheckUser(self,username):
        CanEnterScore = True
        cursor = self.connection.cursor()
        cursor.execute("""
            DECLARE @CanEnterScore BIT;
            EXEC CheckUserAuthority ?,@CanEnterScore= ? OUTPUT
        """, (username,CanEnterScore))
        cursor.commit()
        row = cursor.fetchall()
        if row!=None:
            CanEnterScore = True
        cursor.close()

        if CanEnterScore:
            print("User can enter score.")
            return True
        else:
            print("User cannot enter score.")
            return False
        
    def showSurvey(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT options FROM survey")
        row=cursor.fetchone()
        while(row):
            print(row)
            row=cursor.fetchone()
        cursor.close()


    def Addvote(self,opt):
        cursor = self.connection.cursor()
        cursor.execute("{CALL AddSurvey (?)}", opt)
        self.connection.commit()
        print("Vote saved successfully.")


    def enterGrade(self,username,student_id,grade):
        if(self.CheckUser(username)):
            cursor = self.connection.cursor()
            cursor.execute("{CALL enterGrade (?, ?)}", student_id,grade)
            self.connection.commit()
            print("Grade saved successfully.")


    def SendLetter(self,username,title,body):
        try:
            isSent=0
            cursor = self.connection.cursor()
            cursor.execute("""
                DECLARE @isSent BIT;
                EXEC SendLetter ?, ?,?,@isSent = ? OUTPUT
            """, (username, title,body,isSent))
            cursor.commit()
            if isSent == 0:
                print("Leter sent successfully.")
            else:
                print("Failed to send letter .")
        finally:
            cursor.close()

    def connection_close(self):
        self.connection.close()



program = ConsoleDataBase() 
program.menu()
program.connection_close()




