a = 100
def f1():
    a = 200
    # print(globals().get('a')) #(OR)
    print(globals()['a'])
f1()