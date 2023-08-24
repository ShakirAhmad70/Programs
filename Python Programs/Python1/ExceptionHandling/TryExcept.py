print('stmt-1')

try:
    print(10/0) #Exception code
except ZeroDivisionError:
    print("INFINITE") #Handling code
    
print('stmt-3')