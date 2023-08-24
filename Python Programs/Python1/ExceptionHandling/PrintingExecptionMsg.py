try:
    print('stmt-1')
    print(10/0)
    print("stmt-3")
except ZeroDivisionError as zde :
    print("Exception type is:",type(zde))
    print("Exception class is:",zde.__class__.__name__)
    print("Description of exception is:",zde)
    