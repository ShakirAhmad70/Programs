class Student:
    # def __init__(self):
    #     print("Constructor is executing.........!!!")
    #     self.name = 'Shakir Malik'
    #     self.rollNo = 'GU19R0389'
    #     self.phoneNo = '7078630723'
        
    def __init__(self, name, rollNo, phoneNo):
        self.name = name
        self.rollNo = rollNo
        self.phoneNo = phoneNo
    
    def details(self):
        print('*'*23,"Details of student are",'*'*23)
        print('\t\t\tName is : {}'.format(self.name))
        print('\t\t\tRoll No is : {}'.format(self.rollNo))
        print('\t\t\tPhone No is : {}\n'.format(self.phoneNo))

# s1 = Student()
# print('\nHello my name is :',s1.name)
# print('My roll no is :',s1.rollNo)
# print('My phone no is :',s1.phoneNo,'\n')
# s1.details()

s2 = Student("Sunny", "GU19R0388", '+919045786780')
s2.details()
