import os

#Finally block will definitely get executed whether exception occur, not occur, handled or not handled
try:
    print("Try")
    # print(10/0)
except ValueError: #Exception not handled then also finally will be execute
    print("Except")
finally:
    print("*********************************************")
    print("****************First Finally****************")
    print("*********************************************")

#there are only two situations where finally block won't be executed
#one is power gone situation(PVM termination) power will not wait for pvm to execute finally
#we can terminate PVM manually by os._exit(0) method
try:
    print("Try")
    #os._exit(0)
except ValueError:
    print("Except")
finally:
    print("*********************************************")
    print("***************Second Finally****************")
    print("*********************************************")
    
#and second one is in nested try-catch situation
try:
    print("Outer try")
    print(10/0) #Exception occur here control will go to outer except block directly
    try:
        print("Inner try")
    except:
        print("Inner except")
    finally:
        print("Inner finally") #so this finally block won't be executed 
except:
    print("Outer except")
finally:
    print("Outer finally")