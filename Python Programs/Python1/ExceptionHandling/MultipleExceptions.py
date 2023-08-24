#Handle multiple exception at multiple places
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Division is:",x/y)
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("Please provide int values only")
    
#Handle multiple exception at single place
try:
    x = int(input("Enter first number:"))
    y = int(input("Enter second number:"))
    print("Division is:",x/y)
# except (ZeroDivisionError, ValueError): #should be in the form of tuple
#     print("Exception occur")
#-------------(OR)-------------#
except (ZeroDivisionError, ValueError) as e:
    print("Exception occur")
    print("\t",e.__class__)
    print("\t",e)
