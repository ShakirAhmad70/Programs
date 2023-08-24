from functools import reduce

l = [1,2,3,4,5,6,7,8,9,10]

sum = reduce(lambda x,y : x+y, l) #going to consider 2 2 values from l and it will add them until a single value remains
print(sum)


#sum of first 100 integers
print(reduce(lambda x,y : x+y, range(1,101)))