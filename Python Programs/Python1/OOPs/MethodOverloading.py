#Python won't provide the method overloading concept by default
#But in python we can use one method for multiple types of argument
#Same as we can overload constructor as we overload method

class Test:
    def m1(self, x):
        print(f"{x.__class__.__name__} - argument method")

    def m2(self, a=None, b=None, c=None):  #default arguments
        if a is not None and b is not None and c is not None:
            print('Three args method')
        elif a is not None and b is not None:
            print('Two args method')
        elif a is not None:
            print('One args method')
        else:
            print('No args method')

    def m3(self, *args):  #args will be a tuple
        print('Variable length arguments method')


t = Test()
print("Testing m1 method")
t.m1(12)
t.m1(12.5)
t.m1('as')
t.m1(range(10))
t.m1((12,23,43,345))
t.m1([12,23,43,345])
t.m1({12,23,43,345})
t.m1({12:'a',23:'b',43:'c',345:'d'})

print("\nTesting m2 method")
t.m2(121,12,2)
t.m2(1)
t.m2('str', 123)
t.m2()

print("\nTesting m2 method")
t.m3()
t.m3(12,34,4345,346,654,5,234,234,3)

class Sum:
    def sum(self, *args):
        sum  = 0
        for i in args:
            sum = sum + i
        print('sum is:',sum)
        
print('Example.....!!')        
s = Sum()
s.sum()
s.sum(12)
s.sum(12,12)
s.sum(23,232,-232)