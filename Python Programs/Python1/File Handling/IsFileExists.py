import os.path

fName = input("Enter file name: ")

if os.path.isfile(fName):
    print("File Exists:",fName)
    with open(fName,'r') as f:
        print("Content of file is:")
        print("*"*50)
        text = f.read()
        print(text)
        print("*"*50)
else:
    print("File doesn't exists",fName)
