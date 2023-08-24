import os

currentWorkingDirectory = os.getcwd()
print("Current working directory is:",currentWorkingDirectory)

# os.mkdir("DirectoryCreatedByPythonProgram") #makeDirectory method
# print("Directory created successfully..!!")

# os.mkdir("DirectoryCreatedByPythonProgram/SubDirectoryCreatedByPythonProgram") #compulsory DirectoryCreatedByPythonProgram is already must be created
# print("Sub directory created successfully..!!")

# #if you want to create subdirectories even parent directory is not available make sure you use makedirs() method 
# os.makedirs("Dir/SubDir/SubSubDir")

# os.mkdir("F://ThisDirectoryIsCreatedByPythonProgram")
# print("Directory got created successfully in different disk")

# os.rmdir("Dir/SuBDiR/SubSubdIR") #remove SubSubDir directory
# print("Directory removed successfully")

#If you want to remove parent and sub directories simultaneously make sure you use removedirs() method
# os.removedirs("Dir/SubDir/SubSubDir")
# print("Task Done")

# os.rename("Dir", "Dir1")
# print("Dir directory renamed to Dir1 successfully..!!!")

# os.mkdir("Dir1/SubDir1")
# l = os.listdir("Dir1") #listing all adjacent subdirectories
# print(l)

#Note: create a file(not directory into some directory or subdirectories for better understanding of the output of the program)
g = os.walk("Dir1") #generating all subdirectories
# print(type(g)) #generator
# for x in g:
#     print(x) #x will be in the for of tuple with three elements mention in the below for loop
#for better understanding execute this for loop
for dirpath,dirNames,fileNames in g:
    print(dirpath)
    print(dirNames)
    print(fileNames) 
    print()