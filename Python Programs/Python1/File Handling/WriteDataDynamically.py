fileName = input("Enter file name with extension: ")
f = open(fileName, 'w')
while True:
    data = input("Enter data to write into the file: ")
    f.write(data+"\n")
    option = input("Do you have more data to write into file(y/n): ")
    if option.lower() == 'n':
        break
    else:
        continue
f.close()
