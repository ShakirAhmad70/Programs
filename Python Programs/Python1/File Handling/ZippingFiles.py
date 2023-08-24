from zipfile import *

zf = ZipFile("ZippedFile.zip", 'w', ZIP_DEFLATED)#constant for zipping the files
zf.write('abc.txt')
zf.write('durga.mp4')
zf.write('dynamicData.txt')
zf.write('employee.csv')
print("Zip file created successfully...!!")