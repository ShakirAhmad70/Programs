def generateN(n):
    i = 1
    while i <= n:
        yield i
        i += 1

g = generateN(10)
for x in g:
    print(x)

