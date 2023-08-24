def generateFibonacci(n):
    a,b = 0,1
    while n > 0:
        yield a
        a,b = b, a+b
        n -= 1

g = generateFibonacci(100000)
for x in g:
    print(x)
        