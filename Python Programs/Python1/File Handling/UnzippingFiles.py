from zipfile import *

zf = ZipFile("ZippedFile.zip", "r", ZIP_STORED)
zf.extractall()  # This extracts the files to the current directory
print("Extracted files:")

namesOfFiles = zf.namelist()
for name in namesOfFiles:
    print(name)