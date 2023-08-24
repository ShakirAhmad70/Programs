import pickle

class Employee:
    def __init__(self, eNo, eName, eSal, eAdd):
        self.eNo = eNo
        self.eName = eName
        self.eSal = eSal
        self.eAdd = eAdd
        
    def displayInfo(self):
        print(f"Emp. No: {self.eNo}\nEmp. Name: {self.eName}\nEmp. Salary: {self.eSal}\nEmp. Address: {self.eAdd}")
    
e = Employee(100, "Shakir Malik", 100000000, "Saharanpur")

with open("serEmp.txt", "wb") as f:
    pickle.dump(e, f) #Serialization or Pickling

with open("serEmp.txt", "rb") as f:
    emp_obj = pickle.load(f) #Deserialization or Unpickling

emp_obj.displayInfo()