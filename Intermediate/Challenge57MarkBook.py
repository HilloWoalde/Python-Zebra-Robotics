class Student:
    def __init__(self, firstName, lastName, name, mark = 0): 
        self.firstName = firstName
        self.lastName = lastName
        self.mark = int(mark)
        self.name= firstName + " " + lastName
        
    def setMark(self, mark):
        self.mark = int(mark)
        
    def PrintStudentInformation(self):
        print("Name:", self.firstName + " " + self.lastName)
        print("Mark:", self.mark)

    def PrintStudentName(self):
        print(self.name)

#Aidan = Student("Aidan", "Pereira", "98")
students = []
#students.append(Aidan)
file=open("57Marks.txt", "r")
    #print(file.readlines())
while True:
    currentLine = file.readline()
    if not currentLine:
            break
    line=currentLine.split()
        #line=line.strip("\n][")
    name=line[0].split("-")
    firstName=name[0]
    lastName=name[1]
    mark=line[1]
    student = Student(firstName, lastName, "", mark)
    students.append(student)
while True: 
    menu = input("What would you like to do?\n   1. Add new student\n   2. Update student information\n   3. See Student Information\n   4. Save and Exit\n   5. Top 3 students\n   6. See all student names\n   7. See a list of Failing Students\n   8. See the Average Grade\n")
    
    if menu == "1":
        firstName = input("What is the student's first name? ")
        lastName = input("What is the student's last name? ")
        mark = input("What is the student's mark?")
        students.append(Student(firstName, lastName, "", mark))
    elif menu == "2":
        studentToFind = input("What is the student's first name? ")
        for i in students:
            if (i.firstName == studentToFind):
                newMark = input("What is the student's new grade? ")
                i.setMark(newMark)
    elif menu == "3":
        studentToFind = input("What is the student's first name? ")
        for i in students:
            if (i.firstName == studentToFind):
                i.PrintStudentInformation()
    elif menu == "4":
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
    else: 
        print("Invalid Menu Option")
