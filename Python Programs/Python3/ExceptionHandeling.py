while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("That's not a valid number..!")
    except KeyboardInterrupt:
        print("No input taken..!") #when pressed 'ctrl + c'
    finally:
        print("Attempted Input..!")
    
print("Your Number is:",x)