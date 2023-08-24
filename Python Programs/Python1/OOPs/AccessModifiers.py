class Test:
    def __init__(self) -> None:
        self.x = 20 #public member
        self.__x = 10 #private variable
        self._x = 30 #protected member(can be access outside of class only in child class but it is a naming convention otherwise you can access protected members outside of class anywhere)
        
    def __m1(self): #private method
        print("Private method")

    def m2(self):
        print("private variable:",self.__x)
        self.__m1()
        
    
t = Test()
t.m2()    

# print(t.__x)
print("Accessing private members outside of the class")
print(t._Test__x) #Name Mangling (Accessing private members outside of the class)
t._Test__m1()
        
    