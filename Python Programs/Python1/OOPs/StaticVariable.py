class Student:
    schoolName = "HBH" #static variable (directly)
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        Student.age = 18  #static variable (inside constructor)
    
    principleName = "Vajid" #static variable (directly)

    def m1(self):
        Student.fatherName = 'Vaheed'  #static variable (inside instance method)

    @classmethod
    def m2(cls):
        Student.courseName = 'B.tech'  #static variable (inside class  method)
    
    @staticmethod
    def m3():
        Student.currentYear = 4  #static variable (inside static  method)

    def printStaticInfo(cls):
        print("Static variables are:- ",Student.schoolName, Student.principleName, Student.age, Student.fatherName, Student.courseName, Student.currentYear, Student.currentSemester)


Student.currentSemester = 8 #static variable (outside the class)
s = Student('shakir', 'gu19r0389')
s.m1()
s.m2()
s.m3()
s.printStaticInfo()

# Note: We can access static variable via object reference but can't change its value via object reference