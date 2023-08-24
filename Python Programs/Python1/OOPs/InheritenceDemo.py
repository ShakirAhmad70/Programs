import time

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def waiting(self,newLine, delay, list):
        if newLine.lower() == 'y':
            for i in range(len(list)):
                time.sleep(delay)
                print(list[i])
            time.sleep(1)
        elif newLine.lower() == 'n':
            for i in range(len(list)):
                time.sleep(0.5)
                print(list[i], end=" ")
            time.sleep(1)
        else:
            print("Waiting method not executed...!!")
        print()

    def eatAndDrink(self):
        msg = ["Eating", "Biryani", "and", "Drinking", "Water"]
        self.waiting('n', 0.5, msg)
        


class Employee(Person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal

    def empInfo(self):
        super().waiting('n', 0.5, ["Employee", "Information"])
        super().waiting('y', 1, ["Name: "+self.name, "Age: "+str(self.age), "Employee No: "+self.eno,"Employee Salary: "+str(self.esal)])
        

e = Employee("Tiku", 21, "239849", 110000)
e.eatAndDrink()
e.empInfo()