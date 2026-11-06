from account import Account
from data import accounts

def save_accounts():
    with open("accounts.txt","w") as file:
        for account in accounts:
            file.write(f"{account.account_number}, {account.name}, {account.balance}\n")
from datetime import datetime

def save_transaction(message):
    with open("transactions.txt","a") as file:
        time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        file.write(f"[{time}] {message}\n")

import os
def load_accounts():
    if not os.path.exists("accounts.txt"):
        return
    with open("accounts.txt", "r") as file:
        for line in file:
            account_number, name, balance = line.strip().split(",")
            account = Account(name, int(account_number), float(balance))            
            accounts.append(account)

def generate_account_number():
    if not accounts:
        return 1001
    return max(account.account_number for account in accounts) +1

def find_account(account_number):
    for account in accounts:
        if str(account.account_number) == str(account_number):
            account.display()
            return account
    return None

def is_valid_name(name):
    name = name.strip()
    if not name:
        return False
    return name.replace(" "," ").isalpha()                

def add_account(name, balance):    
    account_number = generate_account_number()
    account = Account(name, account_number, balance)
    accounts.append(account)
    save_accounts()
    save_transaction(
        f"New Account | Account:{account.account_number} | Name: {account.name} |  Balance: {account.balance}")
    print("Account created successfully.")
    print(f"Your Account Number is : {account.account_number}")

def show_accounts():
    if not accounts:
        print("No accounts found")
        return
    print("\n" + "=" * 55 )
    print(f"{'Acc No': <10} {'Name':<20} {'Balance' :>15}")
    print(f"=" * 55)
    for account in accounts:
        print(
            f"{account.account_number:<10}"
            f"{account.name:<20}"
            f"{account.balance:>15.2f}"
        )        
        print("=" * 50)

import os
def show_transactions():
    if not os.path.exists("transactions.txt"):
        print("No transaction history found.")
        return
    with open("transactions.txt", "r")as file:
        content = file.read()
        if content.strip():
            print("\n===== Transaction History=====")
            print(content)
        else:
            print("No transactions yet.")        

def search_account(account_number):
    account = find_account(account_number)
    if account:
        account.display()
    else:        
         print("Account not found")

def search_by_name(name):
    found = False
    for account in accounts:
        if account.name.lower() == name.lower():
            print(account)
            found = True
    if not found:
        print("No account found.")                 

def deposit_to_account(account_number, amount):
    account = find_account(account_number)        
    if account: 
        account.deposit(amount)
        save_accounts()
        save_transaction(f"Deposit | Account:{account.account_number} | Amount: {amount}")        
    else:    
         print("Account not found")

def withdraw_from_account(account_number, amount):
    account = find_account(account_number)        
    if account:
        account.withdraw(amount)
        save_accounts()
        save_transaction(f"Withdraw | Account:{account.account_number} | Amount: {amount}") 
    else:        
         print("Account not found")

def transfer_money(from_account_number, to_account_number, amount):
    sender = find_account(from_account_number)
    receiver = find_account(to_account_number)
    if sender is None:
        print("Sender account not found.")
        return
    if receiver is None:
        print("Receiver account not found.")
        return
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    if sender.balance < amount:
        print("Insufficient balance.")
        return    
    sender.balance -= amount
    receiver.balance += amount
    save_accounts()
    save_transaction(f"Transfer | From: {sender.account_number} | " 
                    f"To: {receiver.account_number} | Amount:{amount}")
    print("Transfer completed succcessfully.")

def check_account_balance(account_number):
    for account in accounts: 
        if str(account.account_number) == str(account.account_number):
            account.check_balance()
            return
    print("Account not found")

def update_account(account_number, new_name):
    account = find_account(account_number)
    if account:
        account.name = new_name
        save_accounts()
        save_transaction(
            f"Update Account | Account :{account.account_number} | New Name: {account.name}")
        print("Account updated successfully")            
    else:
        print("Account not found")

def delete_account(account_number):
    account = find_account(account_number)
    if account: 
        confirm = input("Are you sure you want to delete this account?(y/n): ")
        if confirm.lower() == "y":
            save_transaction(
                f"Delete Account | account:{account.account_number} | Name: {account.name}"
            )
            accounts.remove(account)
            save_accounts()
            print("Account deleted successfully")
        else:
            print("Delete cancelled")
    else:   
        print("Account not found")

def bank_statistics():
        if not accounts:
            print("No accounts found.")
            return
        total_accounts = len(accounts)
        total_balance = sum(account.balance for account in accounts)
        highest_account = max(accounts, key=lambda account: account.balance) 
        lowest_account = min(accounts, key=lambda account: account.balance)
        average_balance = total_balance / total_accounts 
        print("\n===== Bank Statistics ======")
        print(f"Total Accounts :{total_accounts}") 
        print(f"Total Balance : {total_balance:.2f}")
        print(f"Average Balance:{average_balance:.2f}")
        print(f"Highest Balance: {highest_account.name}({highest_account.balance:.2f})")
        print(f"lowest Balance: {lowest_account.name}({lowest_account.balance:.2f})")

