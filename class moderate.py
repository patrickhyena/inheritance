class People():
    __name: str
    __address: str

    def __init__(self, name: str, address: str):
        self.__name = name
        self.__address = address


    def getName(self) -> str:
        return self.__name

    def getAddress(self) -> str:
        return self.__address

    def setAddress(self, address: str) -> str:
        self.__address = address
    
    def toString(self) -> str:
        return self.__name + self.__address

class Student(People):
    __numOfCourses: int = 0
    __courses: [str] = []
    __grades: [int] = []

    def __init__(self, course: str, grade: str):
        People.__init__(self, name = str, address = str)
        __courses = course
        __grades = grade

    def addCourseGrade(self, course: str, grade: str):
        self.__courses.append(course)
        self.__grades.append(grade)

    def printGrades(self):
        for i in range(len(self.__courses)):
            print("Your Score is", self.__grades[i],"in", self.__courses[i])


    def getAverageGrades(self) -> float:
        return self.__grades/ len(self.__grades)

    def toString(self) -> str:
        return "Student: " + super().toString()

class Teacher(People):
    __numOfCourses: int = 0
    __courses : [str] = []

    def __init__(self, name: str, address: str):
        super().__init__(name, address)
        

    def addCourse(self, course: str) -> bool:
        if course in self.__courses == False:
            self.__courses.append(course)
            self.__numOfCourses += 1
            return True
        else:
            return False


    def removeCourse(self, course: str) -> bool:
        if course in self.__courses == True:
            self.__courses.remove(course)
            self.__numOfCourses -= 1
            return True
        else:
            return False


    def toString(self) -> str:
        return "Teacher: " + super().toString() 


newStudent = Student("Vincent","345 Street")

print(newStudent.toString())

newStudent.addCourseGrade("Science", 98)
newStudent.addCourseGrade("Physics", 67)

newStudent.printGrades()

print(newStudent.getAverageGrades())

newTeacher = Teacher("Sir Bagus", "Pak Wince")

print(newTeacher.toString())

print(newTeacher.addCourse("Science"))
print(newTeacher.addCourse("Maths"))
print(newTeacher.addCourse("Maths"))

print(newTeacher.removeCourse("Maths"))
print(newTeacher.removeCourse("Maths"))


    

    

