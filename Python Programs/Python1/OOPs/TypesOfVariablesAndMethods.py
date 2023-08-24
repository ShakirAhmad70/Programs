class Student:
    schoolName = "HBH" #static variable
    
    def __init__(self, name, rollNo):
        self.name = name      #instance variable
        self.rollNo = rollNo  #instance variable
        
    def info(self):
        x = 10  # x is local variable
        for i in range(x): # i is local variable
            print(i)
            
    def studentInfo(self):  #instance method will have only instance variables
        print('Student Name is:',self.name)
        print('Student Roll No is:',self.rollNo)
        
    @classmethod
    def schoolInfo(cls):   #class method will have only static variables
        print('School Name is:',cls.schoolName)
        
    @staticmethod
    def getSum(a,b):  #static method neither have instance variables nor have static variables, this will have only some general purpose variables
        return a+b
        
    
        
        
        
#                                                    ___     
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                                   |   |
#                                           <------------------>
#                                            \                /
#                                             \              /
#                                              \            /
#                                               \          /
#                                                \        /
#                                                 \      /
#                                                  \    /
#                                                   \  /
#                                                    \/