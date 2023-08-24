def squareIt(n):
    return n*n

l = [1,2,3,4,5,6,7,8,9,10]

m = map(squareIt, l)
squareList = list(m)
print('Squares Are:',squareList)