class A:
    def m1(self):
        print("A class m1 method")
class B(A):
    def m1(self):
        print("B class m1 method")
class C(B):
    def m1(self):
        print("C class m1 method")
class D(C):
    def m1(self):
        print("D class m1 method")
class E(D):
    def m1(self):
        # 1.---------------------------------------------------------------------------------#
        # print("E class m1 method")
        
        # 2.---------------------------------------------------------------------------------#
        # super().m1()
        
        #Ta call a particular super class method there are 2 ways we have
        # Note.---------------------------------------------------------------------------------#
        # super().super().m1() ----> This is wrong
        # 1st way ---->  ClassName.methodName(self)
        # B.m1(self)
        # 2nd way ---->  super(ClassName, self).methodName()
        super(C, self).m1()  #method of super class of C will get executed       
        
        
e = E()
e.m1()