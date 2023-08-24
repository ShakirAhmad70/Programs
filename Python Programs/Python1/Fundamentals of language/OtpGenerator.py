from random import *
print("Your OTP for XYZ platform is:",end='')
for i in range(6):
    print(randint(0,9),end='')
    
print('\nOTP with odd digits only:',end='')
for i in range(6):
    print(randrange(1,10,2),end='')


print('\nRandom integer',randint(1,10)) #inclusive

print("Your alphabet OTP is:",end='')
alphabets = "ABCDEFGHIJKLMNOPQRSFTUVWXYZ"
for i in range(6):
    print(choice(alphabets),end='') #sequence should be indexable sequence(list, tuple, string)
