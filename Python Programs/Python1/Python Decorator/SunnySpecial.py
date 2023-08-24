def decorForSunny(fun):
    def inner(name):
        if name.lower() == 'sunny':
            print("#"*30)
            print("Hello Sunny, you are very special for us..!")
            print("Very good morning..!!")
            print("#"*30)
        else:
            fun(name)
    
    return inner

@decorForSunny
def wish(name):
    print("Good morning",name)

wish(input("Enter your name: "))