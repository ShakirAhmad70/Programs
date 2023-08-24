l = [1,2,3,4,5,6,7,8,9,10]

squareList = list(map(lambda n : n*n, l))
print('Squares of {} Are : {}'.format(l,squareList))

l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9,10,11,12]

#map function for multiple sequences
l3 = list(map(lambda x,y : x+y, l1,l2)) #will consider x from l1, and y from l2 and so on is more lists are available
#Note:- Extra elements from l2 will be ignored
print('New List is:',l3)
