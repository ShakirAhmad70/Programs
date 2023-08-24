f = None
try:
    f = open("abc.txt")
except:
    print("There is an error while opening file...!!")
else:
    print("File opened successfully...!!")
    print("The content of the file is:")
    print("#"*30)
    print(f.read())
finally:
    if f is not None:
        f.close()