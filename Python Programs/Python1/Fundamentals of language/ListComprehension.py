#Naive way to create a list
l = [1,2,3,4,5,6,7,8,9,10] 
print(l)

#Many lines of code to create a lisy
l = []
for x in range(1,11):
    l.append(x)
print(l)

#Comprehension way to create a list in just one line of code
#Syntax1: l = [expression for each_element in sequence]
#Syntax2: l = [expression for each_element in sequence if conditoin]
l = [x for x in range(1,11)]
print(l)
l = [x for x in range(1,101) if x%10==0]
print(l)