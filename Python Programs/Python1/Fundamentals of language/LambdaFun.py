#Anonymous Function (OR) Lambda Function
#Syntax:- lambda inout_args : expression
#                     (OR)
# nameOfFun = lambda input_args : expression


square = lambda n : n*n #It is a lambda function which is no more anonymous bcoz i have given it name as 'square'

sum = lambda a,b : a+b

biggerIn2 = lambda a,b : a if a>b else b

biggerIn3 = lambda a,b,c : a if a>b and a>c else b if b>c else c


print(square(4))

print(sum(4,34))

print(biggerIn2(4,34))

print(biggerIn3(12,-34,3))
