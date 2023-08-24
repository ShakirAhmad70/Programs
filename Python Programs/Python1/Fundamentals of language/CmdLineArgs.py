from sys import argv

sum = 0
for x in argv[1:]:
    sum += int(x)

print("Sum is:",sum)