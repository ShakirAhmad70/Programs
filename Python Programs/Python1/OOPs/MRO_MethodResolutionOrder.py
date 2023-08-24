class A:
    pass
class B:
    pass
class C:
    pass
class D(A,B):
    pass
class E(B,C):
    pass
class F(D,E,C): 
    pass


print("mro of A: ",A.mro(),"\n")
print("mro of B: ",B.mro(),"\n")
print("mro of C: ",C.mro(),"\n")
print("mro of D: ",D.mro(),"\n")
print("mro of E: ",E.mro(),"\n")
print("mro of F: ",F.mro(),"\n")