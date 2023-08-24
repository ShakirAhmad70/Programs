# traditional collection
# l = [x*x for x in range(100000)]
#print(type(l))
# print(l)


g = (x*x for x in range(10000000000000000000000000000000000))
# print(type(g))
# while True:
#     print(next(g))
#      OR
for x in g:
    print(x)
    


    