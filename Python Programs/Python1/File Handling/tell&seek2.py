f = open("students.txt", 'w')
f.write("ALL STUDENTS ARE STUPIDS")
f.close()
with open("students.txt", 'r+') as f:
    print("Original Data:", f.read())
    f.seek(17)
    f.write("GEMS!!!")
    f.seek(0)
    print("Modified Data:",f.read())