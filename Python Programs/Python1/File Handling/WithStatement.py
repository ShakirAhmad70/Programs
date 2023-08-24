with open("abc.txt", "w") as f:
    f.write("No need to close this file\n")
    f.write("with statement automatically will close this file")
    print("Data written to the file successfully, Check abc.txt file")
    print(f.closed) #False

print(f.closed) #True