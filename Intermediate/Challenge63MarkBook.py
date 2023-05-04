dates=[]
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def PrintDOB(self):
        print(self.month+" "+self.day+", "+self.year)
class Student:
    def __init__(self, firstName, lastName, name = "", mark = 75, yob="9999", mob="Jan", dob="3th", studentNum = "0000", grade="B", classNum="0", attendance="0", totClasses="0", corrupted=False):  #yob=yr of brith, mob=mth of birth, dob=day of birth
        self.firstName = firstName
        self.lastName = lastName
        self.mark = int(mark)
        self.name = firstName + " " + lastName
        self.dob = Date(dob, mob, yob)
        dates.append(self.dob)
        self.studentNum=studentNum
        self.grade=grade
        self.classNum=classNum
        self.attendance = attendance
        self.totClasses=totClasses
        self.yob=yob
        self.mob=mob
        self.dob=dob
        
    def setGrade(self, grade):
        self.grade = int(grade)
        
    def PrintStudentInformation(self):
        print("Name:\n", self.name)
        print("Mark:\n", self.mark)
        print("DOB:"    )
        #for i in dates:
            #if i.confirm_reality(self.day)
        for i in dates:
            if i == self.dob:
                i.PrintDOB
        dates[0].PrintDOB()
        print("Student Number:\n", self.studentNum)
        print("Grade:\n", self.grade)
        print("classNum:\n", self.classNum)
        a=(str(self.attendance)+" classes attended out of "+str(self.totClasses)+" total classes")
        print("Attendance:\n", a)
        

    def PrintStudentName(self):
        print(self.name)

    def setAttendance(self, totClasse, attended):
        if totClasses == ".":
            pass
        elif "+" in totClasse:
            a = totClasse.split("+")
            self.totClasses+=int(a[0])
        else:
            self.totClasses=totClasse
            
        if attended == ".":
            pass
        elif "+" in attended:
            a = attended.split("+")
            self.attendance+=int(a[0])
        else:
            self.attendance=attended
print(" Please note that in the 63Marks.txt file, students are saved as: \n FirstName-LastName Mark YearOfBirth MonthOfBirth DayOfBirth StudentNumber Grade ClassNumber ClassesAttended TotalClasses Corruption \n If the Corruption value shows as True, please send your file for the corruption to be fixed. \n When adding a student in the file, you only have to add their first and last name, and in the program you must add all values, and any incomplete values in file with be filled with default values.")
#Aidan = Student("Aidan", "Pereira", "98")
students = []
#students.append(Aidan)
f=open("63Marks.txt", "r")
    #print(file.readlines())
while True:
    student=Student("f", "l")
    currentLine = f.readline()
    if not currentLine:
            break
    line=currentLine.split()
        #line=line.strip("\n][")
    name=line[0].split("-")
    firstName=name[0]
    lastName=name[1]
    if len(line) > 1:
        mark=int(line[1])
        if len(line) > 4:
            yob=line[2]
            mob=line[3]
            dob=line[4]
            if len(line) > 5:
                studentNum=line[5]
                if len(line) > 6:
                    grade=line[6]
                    if len(line) > 7:
                        classNum=line[7]
                        if len(line) > 8:
                            attendance=line[8]
                            if len(line) > 9:
                                totClasses=line[9]
                                if len(line) > 10:
                                    corrupted=bool(line[10])
                                    if len(line) > 11:
                                        corrupted=True
                                    student = Student(firstName, lastName, "", mark, yob, mob, dob, studentNum, grade, classNum, attendance, totClasses, corrupted)
                                else:
                                    student = Student(firstName, lastName, "", mark, yob, mob, dob, studentNum, grade, classNum, attendance, totClasses)
                            else:
                                student = Student(firstName, lastName, "", mark, yob, mob, dob, studentNum, grade, classNum, attendance)
                        else:
                            student = Student(firstName, lastName, "", mark, yob, mob, dob, studentNum, grade, classNum)
                    else:
                        student = Student(firstName, lastName, "", mark, yob, mob, dob, studentNum, grade)
                else:
                    student = Student(firstName, lastName, "", mark, yob, mob, dob, studentNum)
            else:
                student = Student(firstName, lastName, "", mark, yob, mob, dob)
        else:
            student = Student(firstName, lastName, "", mark)
        
    else:
        student = Student(firstName, lastName, "")

    students.append(student)
f.close()
while True: 
    menu = input("What would you like to do?\n   1. Add new student\n   2. Update student Grade\n   3. See Student Information\n   4. Save and Exit\n   5. Top 3 students\n   6. See all student names\n   7. See a list of Failing Students\n   8. See the Average Grade\n   9. Update student Attendance")
    
    if menu == "1":
        firstName = input("What is the student's first name? ")
        lastName = input("What is the student's last name? ")
        mark = input("What is the student's mark?")
        yob=input("What year was the student born?")
        mob=input("What day was the student born?")
        dob=input("What month was the student born?")
        studentNum=input("What is the student's student number?")
        grade=input("What is the student's grade?")
        classNum=input("What is the student's class number?")
        students.append(Student(firstName, lastName, "", mark, yob, mob, dob, studentNum, grade, classNum, 0, 0))
    elif menu == "2":
        studentToFind = input("What is the student's student number? ")
        for i in students:
            if (i.studentNum == studentToFind):
                grade = input("What is the student's new grade? ")
                i.setGrade(grade)
    elif menu == "3":
        studentToFind = input("What is the student's student number? ")
        for i in students:
            if (i.studentNum == studentToFind):
                i.PrintStudentInformation()
    elif menu == "4":
        file=open("63Marks.txt", "w")
        text=""
        for i in students:
            fname=i.firstName
            lname=i.lastName
            mark=i.mark
            print("Writing the following to the file:" + fname+"-"+lname+" "+str(mark)+yob+mob+dob+studentNum+grade+classNum+attendance+totClasses+corruption)
            text+=(fname+"-"+lname+" "+str(mark)+yob+mob+dob+studentNum+grade+classNum+attendance+totClasses+corruption+"\n")
        file.write(text)
        print(text)
        file.close()
        break;
    elif menu == "5":
        counter = 0
        for i in range(100, -1, -1):
            if counter == 3:
                break;
            for x in students:
                if (x.mark == i):
                    counter += 1
                    print("The Student with Rank " + str(counter) + " is:")
                    x.PrintStudentInformation()
    elif menu == "6":
        for i in students:
            i.PrintStudentName()
    elif menu == "7":
        failGrade = int(input("Below what is a failing grade?"))
        for i in students:
            if i.mark < failGrade:
                i.PrintStudentInformation()
    elif menu == "8":
        total=0
        studentnum=0
        for i in students:
            total += i.mark
            studentnum += 1
        print("The Average Grade is " + str(total/studentnum))
    elif menu == "9":
        studentToFind = input("What is the student's student number? ")
        for i in students:
            if (i.studentNum == studentToFind):
                i.setClasses(input("How many classes have occered? (press . to not change, and do + to add how many more classes of this student's have passed. Do just a number to set it to that number.)"), input("How many classes has the student appeared in? (press . to not change, and do + to add how many more classes of this student's have passed. Do just a number to set it to that number.)"))
    else: 
        print("Invalid Menu Option")
