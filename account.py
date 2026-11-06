class Account:
    def __init__(self, name,account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        

    def display(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

    def deposit(self,amount):
        if amount <= 0:
            print("Amount must greater than 0")
            return
        self.balance += amount
        print("Deposite succssful")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must greater than 0")
            return
        if amount <= self.balance:
            self.balance -= amount
            print("withdraw successful")
        else:
            print("Insufficient balance") 

    def check_balance(self):
        print(f"Current balance:{self.balance}") 

                        

                            