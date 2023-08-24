l1 = [10, 20, 30]

l1.append(40)
print(l1)

l1.insert(2,25)
print(l1)

l2 = [50, 60]
l1.append(l2) #look at this dude
print(l1)

l2.extend(l1)
print(l2)
# It seems that the ellipsis (...) is displayed in the output as a representation of a self-referential 
# list, indicating that the list contains a reference to itself. This representation is used to prevent 
# infinite recursion in certain cases when printing lists with circular references.

l2.remove(l2) #self referenced data is removed(remove function remove first occurance of data only on all)
print(l2)

print(l1)
print(l1.pop()) #last element will be removed and returned
print(l1)
print(l1.pop(2)) #remove and return the element present at index 2
print(l1)

l1.clear()
print(l1)

l3 = [1,2,3,4,5,6]
l3.reverse()
print(l3)

r = reversed(l3)
l4 = list(r)
print(l4)
print(l3)

l5 = [2,32,12,22,45]
l5.sort() #list member should be homogenious for sort method
print(l5)
print(l5.sort(reverse=True))

l6 = [2,32,12,22,45]
l7 = sorted(l6) #list member should be homogenious for sorted method
print(l7)