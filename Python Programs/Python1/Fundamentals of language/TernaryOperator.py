a = int(input("Enter First Value: "))
b = int(input("Enter Second Value: "))
min = a if a<b else b
print("min value is: ", min)

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
min = a if a<b and a<c else b if b<c else c
print("min value is: ", min)