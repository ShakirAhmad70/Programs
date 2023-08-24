a = 10
print(type(a))  #int

a = 10.5
print(type(a))  #float

a = 10 + 5j
print(type(a)) #complex
#functions in complex class
# print(type(a.real))
# print(type(a.imag))
# print(type(a.conjugate))

a = True
print(type(a))  #bool

a = "Shakir"
print(type(a))  #string

a = [10, 20, 23, "lion"]
print(type(a)) #list


a = (1,2,3)
print(type(a))  #tuple(it is an immutable list)

#special case
a = (10)
print(type(a)) #type is 'int' not tuple

#to make a single value tuple we have to add a comma after value
a = (10,)
print(type(a)) #special case, type is 'int'

a = {2,32,4}
print(type(a))  #set

a = {12:23, 121:23}
print(type(a))  #dictionary

#special case
a = {}  #it is an empty 'dictionary' not an empty 'set', 
        #bcoz dict is more in use in real world as compare to set
print(type(a))

#then how to create an empty set
a = set() #set function is used to create the empty set
print(type(a))

a = {10, 20, 'shakir'}
fs = frozenset(a)
print(type(fs)) #frozen set(it is an immutable version of set)

a = range(10)
print(type(a)) #range

a = [10,20,30]
b = bytes(a)
print(type(b)) #bytes(values: from 0 to 255 only)

a = [12,32]
ba = bytearray(a)
print(type(ba)) #bytearray(it is a mutable version of bytes data type)

a = None
print(type(a)) #NoneType