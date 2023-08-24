def decorForAdd(fun):
    def decoration(a,b):
        print("#"*29)
        print("\tThe Sum is:",end="")
        fun(a,b)
        print("#"*29)
    return decoration

@decorForAdd
def add(a,b):
    print(a+b)

add(2,3)