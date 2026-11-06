
from operations import is_valid_name
from operations import load_accounts
from config import USERNAME, PASSWORD, MAX_LOGIN_ATTEMPTS
attempts = MAX_LOGIN_ATTEMPTS
from operations import(
    add_account,
    show_accounts,
    search_account,
    deposit_to_account,
    withdraw_from_account,
    check_account_balance,
    update_account,
    delete_account,
    transfer_money,
    show_transactions,
    bank_statistics
)

while attempts > 0:
    print("\n===== Bank Mangement SYSTEM =====")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == USERNAME and password == PASSWORD:
        print("\nLogin Successful.\n")
        break
    attempts -= 1
    print("Invalid Ussername or Password.")
    print(f"Remaining Attempts: {attempts}")
if attempts == 0:
    print("Too many failed attempts.")
    exit()
    
load_accounts()
while True:
    print("\n===== Bank Management System=====")
    print("1. Add Account")
    print("2. Show Accounts")
    print("3. Search Account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Check Balance")
    print("7. Update Account")
    print("8. Delete Account")
    print("9.Transfer Money")
    print("10.Show Transactions")
    print("11. Bank Statistics")
    print("12. Exit")
    
    choice = input("Enter your choice: ") 

    if choice =="1":
        name = input("Enter name: ").strip()        
        print("Name cannot be empty")        
        if not is_valid_name(name):
            print("Invalid name")  
            continue            
        try:
            balance = float(input("Enter initial balance: "))
            if balance < 0:
                print("Balance cannot be negative")
                continue
        except ValueError:
            print("Balance must be number")
            continue
        add_account(name, balance) 

    elif choice == "2":
        show_accounts()
        

    elif choice == "3":
        account_number = input("Enter account number: ")
        search_account(account_number)

    elif choice == "4":
        account_number = input("Enter account number: ")
        try:
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
               print("Amount must be greater than 0")
               continue
        except ValueError: 
            print("Amount must be a number")
            continue
        deposit_to_account(account_number, amount)
   
    elif choice == "5":
        account_number = input("Enter account number: ")
        try:
            amount = float(input("Enter withdraw amount: "))
            if amount <= 0:
               print("Amount must be greater than 0")
               continue
        except ValueError: 
            print("Amount must be a number")
            continue
        withdraw_from_account(account_number, amount) 

    elif choice == "6":
        account_number = input("Enter account number: ")
        check_account_balance(account_number)

    elif choice =="7":
        account_number = input("Enter account number: ")
        new_name = input("Enter new name: ").strip()
        if not is_valid_name(new_name):
            print("Invalid name")
            continue  
        update_account(account_number,new_name)

    elif choice == "8":
        account_number = input("Enter account number: ")
        delete_account(account_number)

    elif choice == "9":
        from_account = int(input("Enter sender account number:"))
        to_account = int(input('Enter receiver account number:'))
        amount = float(input("Enter amount to transfer"))
        transfer_money(from_account, to_account, amount)

    elif choice == "10":
        show_transactions()

    elif choice == "11":
        bank_statistics()        

    elif choice == "12":
        print("Thank you for using Bank Management System")
        break
    else:
        print("Invalid choice.please try again.")
            
            




