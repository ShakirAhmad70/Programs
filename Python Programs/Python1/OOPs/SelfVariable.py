#Self variable contain the adress of current variable, self is not a keyword you can use any name in place of self

class demo:
    def __init__(self):
        print("Adress of self:",id(self))
        
    def talk(name, self): #Magic, here first var will be going contain the address of current object i.e. name
        print("Hello my name is:",self) #self is the parameter passed to talk function during function call

d = demo()
print("Adress of d is:",id(d),'\n')

s = demo()
print("Adress of s is:",id(s))

print("\n","*"*80,"\nHence proved that the self variable contain the adress of current variable...!!!\n","*"*80,'\n',sep="")

s.talk("Shakir")