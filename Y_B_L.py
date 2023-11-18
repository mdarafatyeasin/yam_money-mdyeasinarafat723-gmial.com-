class Bank :
        total_admin = []
        total_accounts = []
        total_bank_balance = 0
        total_loan = 0
        loan_facility = True
        is_bankrupt = False

class User:
    def __init__(self, name, password) -> None:
        self.name = name
        self.password = password
        Bank.total_admin.append({"name":name,"password":password})

    # ======================== ADMIN ========================== #

    # ---------------------- create account ---------------------- #
    def create_account (self, name, email, address, accountType, password):
        newAccount = {
            "name" : name,
            "email" : email,
            "address" : address,
            "accountType" : accountType,
            "password" : password,
            "accountNumber" : f'AC-00{len(Bank.total_accounts)+1}',
            "balance" : 0,
            "trHistory" : [],
            "loanCount" : 2
            }
        Bank.total_accounts.append(newAccount)
        print("\nAccount created successfully")

    
    # ---------------------- delete account ---------------------- #
    def delete_account(self, accountNumber):
        found = False
        for user in Bank.total_accounts:
            if(user['accountNumber'] == accountNumber):
                Bank.total_accounts.remove(user)
                found = True
                break
        if found :
            print("\nDelete Success")
        else:
            print("\nUser Not Found")


    # ---------------------- show all account ---------------------- #
    def show_all(self):
        print("=======================================================================")
        for user in Bank.total_accounts:
            print(f"Name: {user['name']} | Account Number: {user['accountNumber']} | Available Loan: {user['loanCount']} | Balance: {user['balance']}")
        print("=======================================================================")
    


    # ---------------------- show bank balance ---------------------- #
    def show_balance(self):
        print('============== BALANCE ==============')
        balance = 0
        for user in Bank.total_accounts:
            balance += user["balance"]
        print("\n")
        print(balance)
    

 
    # ---------------------- show bank loan ---------------------- #
    def show_loan(self):
        print('============== LOAN GIVEN ==============')
        print(f"\nAmount: {Bank.total_loan}")
    


    # ---------------------- off bank loan ---------------------- #
    def off_loan(self):
        print('============== LOAN SYSTEM ==============')
        Bank.loan_facility = False
        print("\nLoan facility is turn off")
    

    
    # ---------------------- bankrupt ---------------------- #
    def bankrupt(self):
        print('============== BANKRUPT ==============')
        Bank.bankrupt = True
        print("\nBankrupt Success")



    # ======================== CUSTOMER ========================== #

    # ---------------------- deposit ---------------------- #
    def add_balance(self, account_number, deposit_amount):
        userAccount = None
        for user in Bank.total_accounts:
            if user["accountNumber"] == account_number:
                userAccount = user
        userAccount["balance"] += deposit_amount
        Bank.total_bank_balance += deposit_amount
        print("\n Deposit Success")


    # ---------------------- check balance ---------------------- #
    def check_balance (self, account_number):
        for user in Bank.total_accounts:
            if user["accountNumber"] == account_number:
                print('============== BALANCE ==============')
                print(user["balance"])


    # ---------------------- withdraw ---------------------- #
    def withdraw (self, account_number, withdraw_amount):
        userAccount = None
        if Bank.is_bankrupt == False:
            for user in Bank.total_accounts:
                if user["accountNumber"] == account_number:
                    userAccount = user
            if userAccount["balance"] >= withdraw_amount:
                userAccount["balance"] -= withdraw_amount
                Bank.total_bank_balance -= withdraw_amount
                transition_status = {"Withdraw":withdraw_amount}
                userAccount["trHistory"].append(transition_status)
                print("\n Withdraw Success")
            else:
                print("\nWithdrawal amount exceeded")
        else:
            print("\nBankrupt")

 
    # ---------------------- transfer balance ---------------------- #
    def transfer_balance (self, account_number, receiverAccount_number, transfer_amount):
        userAccount = None
        receiverAccount = None
        for user in Bank.total_accounts:
            if user["accountNumber"] == account_number:
                userAccount = user
        
        for user in Bank.total_accounts:
            if user["accountNumber"] == receiverAccount_number:
                receiverAccount = user
            else:
                print("\nAccount does not exist")

        if receiverAccount != None:
            if Bank.is_bankrupt == False:
                if userAccount["balance"] >= transfer_amount:
                    userAccount["balance"] -= transfer_amount
                    receiverAccount["balance"] += transfer_amount
                    transition_status = {"Transfer":transfer_amount}
                    userAccount["trHistory"].append(transition_status)
                    print("\n Transfer Amount Successfully")
                else:
                    print("\nNot Enough Balance")
            else:
                print("\nBankrupt")


    # ---------------------- take loan ---------------------- #
    def take_loan(self, account_number, loan_amount):
        userAccount = None
        for user in Bank.total_accounts:
            if user["accountNumber"] == account_number:
                userAccount = user
        if Bank.loan_facility == True:
            if userAccount["loanCount"] != 0:
                userAccount["loanCount"] -= 1
                userAccount["balance"] += loan_amount
                Bank.total_bank_balance += loan_amount
                Bank.total_loan += loan_amount
                print("\nLoan Success")
            else:
                print("\nAlready taken twice")
        else:
            print("\nCurrent loan system is off")

    # ---------------------- transaction history ---------------------- #   
    def transaction_history (self, account_number):
        userAccount = None
        for user in Bank.total_accounts:
            if user["accountNumber"] == account_number:
                userAccount = user 
        print("\n============ Transaction History ============\n")
        for transaction in userAccount["trHistory"]:
            for key, value in transaction.items():
                print(f"{key} => {value}")
    


bank1 = Bank()

Admin = User('admin', '123')

Admin.create_account('yeasin', 'yeasin@yam.com', 'cmc', 'sva', '123')
# Admin.create_account('arafat', 'arafat@yam.com', 'cmc', 'sva', '456')
# Admin.create_account('arafat', 'arafat@yam.com', 'cmc', 'sva', '789')
# Admin.add_balance('AC-002',2000)
# Admin.add_balance('AC-002',2000)
# Admin.check_balance('AC-002')
# Admin.withdraw('AC-002',100)
# Admin.take_loan('AC-002',10)

# Admin.delete_account('AC-002')
# Admin.show_all()
# Admin.show_balance()
# Admin.show_loan()
# Admin.off_loan()
# Admin.bankrupt()


# print(bank1.bankrupt)     
currentUser = None

while True:
    print("================ Log In ================")
    print("1. Customer")
    print("2. Admin")
    op = int(input('Enter account type: '))
    if currentUser == None:
        if op == 1:
            name = input('Enter Name: ')
            password = input('Enter Password: ')
            for customer in bank1.total_accounts:
                if name == customer["name"] and password == customer["password"]:
                    currentUser = customer
                    while True:
                        print("\n1. Deposit")
                        print("2. Check Balance")
                        print("3. Withdraw")
                        print("4. Transfer balance")
                        print("5. Take a Loan")
                        print("6. Transition History")
                        print("7. Log Out\n")
                        op = int(input("Select a option: "))
                        if op == 1:
                            amount = int(input("Enter Amount: "))
                            Admin.add_balance(currentUser["accountNumber"], amount)
                        elif op == 2:
                            Admin.check_balance(currentUser["accountNumber"])
                        elif op == 3:
                            amount = int(input("Enter Amount: "))
                            Admin.withdraw(currentUser["accountNumber"], amount)
                        elif op == 4:
                            transfer_account = input("Enter transfer account number: ")
                            amount = int(input("Enter Amount: "))
                            Admin.transfer_balance(currentUser["accountNumber"], transfer_account, amount)
                        elif op == 5:
                            amount = int(input("Enter Amount: "))
                            Admin.take_loan(currentUser["accountNumber"], amount)
                        elif op == 6:
                            Admin.transaction_history(currentUser["accountNumber"])
                        elif op == 7:
                            currentUser = None 
                            break
        elif op == 2:
            print('Admin\n')
            name = input('Enter Name: ')
            password = input('Enter Password: ')
            for admin in bank1.total_admin:
                if name == admin["name"] and password == admin["password"]:
                    currentUser = admin
                    while True:
                        print('\n1. Create Account')
                        print('2. Delete Account')
                        print('3. All Account')
                        print('4. Bank Balance')
                        print('5. Total Loan Given')
                        print('6. Off Loan System')
                        print('7. Bankrupt')
                        print('8. Log Out\n')
                        op = int(input('Select an option: '))
                        if op == 1:
                            print("create account")
                            name = input("Enter Name: ")
                            email = input("Enter Email: ")
                            address = input("Enter Address: ")
                            account_type = input("Enter Account Type: ")
                            password = input("Enter Password: ")
                            Admin.create_account(name, email, address, account_type, password)
                        elif op == 2:
                            delete_account = input("Enter account number: ")
                            Admin.delete_account(delete_account)
                        elif op == 3:
                            Admin.show_all()
                        elif op == 4:
                            Admin.show_balance()
                        elif op == 5:
                            Admin.show_loan()
                        elif op == 6:
                            Admin.off_loan()
                        elif op == 7:
                            Admin.bankrupt()
                        elif op == 8:
                            currentUser = None  # Correct the assignment
                            break  # Exit the inner loop
                else:
                    print('Wrong ID/Password')