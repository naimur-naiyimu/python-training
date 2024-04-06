accounts = {}

def create_account(account_number, account_holder, initial_balance):
    if account_number not in accounts:
        accounts[account_number] = {
            'account_holder': account_holder,
            'balance': initial_balance
        }
        print(f"Account created successfully for {account_holder} with account number {account_number}.")
    else:
        print("Account already exists with this account number.")

def login(account_number):
    if account_number in accounts:
        print(f"Logged in successfully. Welcome, {accounts[account_number]['account_holder']}!")
        return True
    else:
        print("Account not found.")
        return False

def check_balance():
    if logged_in_account:
        print(f"Current balance: {accounts[logged_in_account]['balance']}.")
    else:
        print("Not logged in. Please log in first.")

def send_money(recipient_account, amount):
    if logged_in_account:
        if recipient_account in accounts:
            if accounts[logged_in_account]['balance'] >= amount:
                accounts[logged_in_account]['balance'] -= amount
                accounts[recipient_account]['balance'] += amount
                print(f"Money sent successfully. New balance: {accounts[logged_in_account]['balance']}.")
            else:
                print("Insufficient funds.")
        else:
            print("Recipient account not found.")
    else:
        print("Not logged in. Please log in first.")

def cash_out(amount):
    if logged_in_account:
        if accounts[logged_in_account]['balance'] >= amount:
            accounts[logged_in_account]['balance'] -= amount
            print(f"Cash out successful. New balance: {accounts[logged_in_account]['balance']}.")
        else:
            print("Insufficient funds.")
    else:
        print("Not logged in. Please log in first.")

logged_in_account = None

while True:
    print("Options:")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account_number = int(input("Enter account number: "))
        account_holder = input("Enter account holder name: ")
        initial_balance = float(input("Enter initial balance: "))
        create_account(account_number, account_holder, initial_balance)

    elif choice == 2:
        account_number = int(input("Enter account number: "))
        login_result = login(account_number)
        if login_result:
            logged_in_account = account_number  # Assign the account number, not True
            while True:
                    print("\nLogged-in Options:")
                    print("1. Check Balance")
                    print("2. Send Money")
                    print("3. Cash Out")
                    print("4. Logout")

                    login_choice = int(input("Enter your choice: "))

                    if login_choice == 1:
                        check_balance()

                    elif login_choice == 2:
                        recipient_account = int(input("Enter recipient account number: "))
                        amount = float(input("Enter amount to send: "))
                        send_money(recipient_account, amount)

                    elif login_choice == 3:
                        amount = float(input("Enter amount to cash out: "))
                        cash_out(amount)

                    elif login_choice == 4:
                        logged_in_account = None
                        print("Logged out successfully.")
                        break

    elif choice == 3:
        break
