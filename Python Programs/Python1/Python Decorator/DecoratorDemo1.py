def myDecor(fun):
    def outputFun():
        print("Sending the person into the beauty parlour")
        print("Showing a person with decoration..!")
        
    fun()
    return outputFun


@myDecor
def display():
    print("Showing a function as it is..!")
# Either you write @myDecor or write in the below way
# display = myDecor(display) #but now display method will loose its own definition
display()