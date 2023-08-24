class Test:
    def __init__(self):
        self.a=10
        self.b=20
        
    def m1(self):
        self.c=30
        
t = Test() # a,b will be added to the object
t.m1() # c will be added to the object
t.d=40 # d will be added to the object
print(t.__dict__) #printing instance variables of object 't'