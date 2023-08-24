try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Result is:",x/y)
except ZeroDivisionError:
    print("ZeroDivisionError handled : division by zero")
except: #default except block must be at last
    print("Default Exception : provide only int value")