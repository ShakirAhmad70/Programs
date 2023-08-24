import os

fName = input("Enter file name with extension: ")

if os.path.isfile(fName):
    print("File exists",fName)
    with open(fName, 'r') as f:
        lCount = wCount = cCount = 0
        
        for line in f:
            lCount = lCount + 1
            noOfWordsInCurrentLine = len(line.split())
            wCount += noOfWordsInCurrentLine
            noOfCharsInCurrentLine = len(line)
            cCount += noOfCharsInCurrentLine
        
        print("No of lines in file are:",lCount)
        print("No of words in file are:",wCount)
        print("No of characters in file are:",cCount)
        
else:
    print("File doesn't exists..!!")
