x = input("Enter Something: ")
print(type(x))

#Read boolean data from keyboard
x = bool(input("Are you married?[Treu/False]: "))
print(x) #see the magic with False value

#bool('') --> will return False
#bool('True),bool('False'), bool('anything non empty') --> will going to return True

#to resolve this problem we use eval() method
x = eval(input("Are you married?[Treu/False]: "))
print(x) #see the magic with False value


#Reading multiple values from keyboard
a, b = [int(x) for x in input("Enter Two Numbers: ").split()]
print("Sum is:",a+b)
