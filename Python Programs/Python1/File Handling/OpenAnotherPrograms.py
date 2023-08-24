#We can run any command from a python program using system() function from os module
#Syntax: os.system("Write any command string here")


import os, time

os.system("dir")
os.system("notepad")
os.system("code")
os.system("powercfg batteryreport")
os.system("battery-report.html")
print("Executing another programs")
os.system('py demo.py')
print("Compiling Java program")
os.system("javac HelloWorld.java")
print("Executing Java program")
os.system("java HelloWorld")



time.sleep(5)
# os.system("cls")
