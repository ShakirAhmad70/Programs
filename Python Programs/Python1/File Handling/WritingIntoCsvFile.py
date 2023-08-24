import csv

with open("employee.csv",'w', newline='') as f:
    w = csv.writer(f)
    # print(type(w))
    w.writerow(['ENO',"ENAME","ESAL","EAGE"])
    while True:
        eNo = int(input("Enter employee no: "))
        eName = input("Enter employee name: ")
        eSalary = float(input("Enter employee salary: "))
        eAge = int(input("Enter employee age: "))
        w.writerow([eNo, eName, eSalary, eAge])
        option = input("Want to add more employee data? (y/n): ")
        if option.lower() == 'n':
            break
