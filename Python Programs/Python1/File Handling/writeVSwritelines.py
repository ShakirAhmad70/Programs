f = open("write.txt", 'w')
f.write("This\n")
f.write("is the\n")
f.write("write\n")
f.write("method's\n")
f.write("content\n")

fw = open("writelines.txt", 'w')
l = ["This\n", "is the\n", "writelines\n", "method's\n", "content\n"]
fw.writelines(l)

print("Data written to files successfully....!!")

f.close()
fw.close()