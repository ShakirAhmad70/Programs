class Customer:
    bankName = 'Shak Bank Of India'
    def __init__(self, name, balance = 0.0) -> None:
        self.name = name
        self.balance = balance
    def deposit(self,amount) -> None:
        self.balance += amount
        print('After deposit, balance is:',self.balance)
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient fund, can't perform the operation...!!")
        else:
            self.balance -= amount
            print("After withdraw, balance is:",self.balance)
    def knowBalance(self):
        print("Your Current balance is:",self.balance)
    
print("Welcome to",Customer.bankName)
name = input("Enter your name: ")
c = Customer(name)
print("Hello",name,"❤️")
while True: 
    print("d - deposit some amount\nw - withdraw some amount\nb - know your balance\ne - exit")
    option = input("Choose your option: ")
    if option.lower() == 'd':
        amount = float(input("Enter your amount: "))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input("Enter your amount: "))
        c.withdraw(amount)
    elif option.lower() == 'b':
        c.knowBalance()
    elif option.lower() == 'e':
        print("Thanks for banking...!!")
        break
    else:
        print("You've chosen a wrong option, please choose an option from the given list")