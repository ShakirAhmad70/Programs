f = open("write.txt", 'r')

# print(f.read()) #read complete data
# print(f.read(10)) #read 10 characters
# print(f.read(-123)) #Read complete data
# print(f.readline()) #read one line
l = f.readlines() #read line by line all lines in the list
for line in l:
    print(line, end="")

f.close()