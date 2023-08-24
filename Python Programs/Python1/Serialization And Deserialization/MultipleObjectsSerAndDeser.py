import pickle, os

class Employee:
    def __init__(self, eNo, eName, eSal, eAdd):
        self.eNo = eNo
        self.eName = eName
        self.eSal = eSal
        self.eAdd = eAdd
        
    def displayInfo(self):
         print(f"Emp. No: {self.eNo}\nEmp. Name: {self.eName}\nEmp. Salary: {self.eSal}\nEmp. Address: {self.eAdd}\n")


#Serialization
while True:   
    eNo = int(input("Enter Employee No: "))
    eName = str(input("Enter Employee Name: "))
    eSal = float(input("Enter Employee Salary: "))
    eAdd = str(input("Enter Employee Address: "))
    e = Employee(eNo, eName, eSal, eAdd)
    with open("serializable.ser", "wb") as f:
        pickle.dump(e, f)
    
    option = input("Want to serialize more data[y/n]: ")
    if option.lower() == 'n':
        break

print("Serialization completed...!!")    


#Deserialization
while True:
    try:
        with open("serializable.ser", "rb") as f:
            emp = pickle.load(f)
            emp.displayInfo()
    except EOFError:
        break

print("Deserialization completed...!!")    
