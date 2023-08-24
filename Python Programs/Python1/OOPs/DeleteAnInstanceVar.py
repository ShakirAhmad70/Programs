class Demo:
    def __init__(self) -> None:
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40
        
    def deleteInClass(self): #you have to use self
        del self.a #this will delete for all objects

print('Total instance variables:')
d = Demo()
print(d.__dict__)

print('After deleting "a"')
d.deleteInClass()
print(d.__dict__)

print('After deleting "b"')
del d.b #delete outside of the class (this will get deleted for a particular object)
print(d.__dict__)