import sys
print(sys.getrecursionlimit())

def fact(n):
    if n == 0: return 1
    else: return n*fact(n-1)
    
print(fact(5)) #6 time recursion call
print(fact(100)) #101 time recursion call
print(fact(999)) #1000 time recursion call so this will produce RecursionError