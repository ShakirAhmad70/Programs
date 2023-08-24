#List is unhashable so we can't add it to the set or dict data structure(as key in dict)
#Tuple is hashable so we can add it to the set as well as to the dict key

import collections
l = [10,20,30,40]
t = (10,20,30,40)
# print(isinstance(l, collections.Hashable)) #now it(Hashable) is depricated after 3.8 version of python
# print(isinstance(t, collections.Hashable)) #now it(Hashable) is depricated after 3.8 version of python
print(hash(t)) #hash code will be returned
#print(hash(l)) #it is unhashable so no hash code is going to be returned


#Examples
s = {10,20}
s.add(t)
print(s)
# s.add(l)
# print(s)

d = {}
d[t] = 'A'
print(d)
d[l] = 'A'
print(d)