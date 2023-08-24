def myGen():
    yield 'A'
    yield 'B'
    yield 'C'

g = myGen()
print(type(g))
try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration as e:
    print("No more values")
