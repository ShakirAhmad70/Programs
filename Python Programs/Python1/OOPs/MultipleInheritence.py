class P1:
    def m1(self):
        print('Parent 1 method')
class P2:
    def m1(self):
        print('Parent 2 method')

# class C(P1, P2):  #P1 method will get the chance
class C(P2, P1):  #P2 method will get the chance
    def m2(self):
        print('Child method')

C().m1()