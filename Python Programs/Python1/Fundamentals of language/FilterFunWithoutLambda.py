def isEven(n):
    if n%2==0 : return True
    else : return False
    
def isOdd(n):
    if n%2==1 : return True
    else : return False

l = [1,2,3,4,5,6,7,8,9,10]

#Syntax of filter fun:- 
#               filter(function, sequence) and it will return a filter object

f = filter(isEven, l)
listOfEven = list(f)
print("Even Numbers are:",listOfEven)

f = filter(isOdd, l)
listOfOdd = list(f)
print("Odd Numbers are:",listOfOdd)