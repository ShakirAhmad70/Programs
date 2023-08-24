l = [1,2,3,4,5,6,7,8,9,10]
listOfEven = list(filter(lambda n : n%2==0, l))
listOfOdd = list(filter(lambda n : n%2==1, l))

print("Even Numbers are:",listOfEven)
print("Odd Numbers are:",listOfOdd)