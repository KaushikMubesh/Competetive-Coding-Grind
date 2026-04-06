class BankAccount:
    def __init__(self, account_number, name, password, balance=0):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ ₹{amount} deposited successfully.")
        else:
            print("❌ Invalid amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance.")
        elif amount <= 0:
            print("❌ Invalid amount.")
        else:
            self.balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.balance}")

    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: ₹{self.balance}")


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            print("❌ Account already exists.")
            return

        name = input("Enter Name: ")
        password = input("Set Password: ")
        account = BankAccount(acc_no, name, password)
        self.accounts[acc_no] = account
        print("✅ Account created successfully.")

    def login(self):
        acc_no = input("Enter Account Number: ")
        password = input("Enter Password: ")

        account = self.accounts.get(acc_no)

        if account and account.password == password:
            print(f"✅ Welcome {account.name}!")
            self.account_menu(account)
        else:
            print("❌ Invalid login credentials.")

    def account_menu(self, account):
        while True:
            print("\n--- Account Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transfer Money")
            print("5. Account Details")
            print("6. Logout")

            choice = input("Enter choice: ")

            if choice == '1':
                amount = float(input("Enter amount: "))
                account.deposit(amount)

            elif choice == '2':
                amount = float(input("Enter amount: "))
                account.withdraw(amount)

            elif choice == '3':
                account.check_balance()

            elif choice == '4':
                self.transfer_money(account)

            elif choice == '5':
                account.display_details()

            elif choice == '6':
                print("👋 Logged out.")
                break

            else:
                print("❌ Invalid choice.")

    def transfer_money(self, sender):
        receiver_acc_no = input("Enter Receiver Account Number: ")
        receiver = self.accounts.get(receiver_acc_no)

        if not receiver:
            print("❌ Receiver account not found.")
            return

        amount = float(input("Enter amount to transfer: "))

        if amount <= 0:
            print("❌ Invalid amount.")
        elif amount > sender.balance:
            print("❌ Insufficient balance.")
        else:
            sender.balance -= amount
            receiver.balance += amount
            print(f"✅ ₹{amount} transferred to {receiver.name} successfully.")


# Main Program
bank = BankSystem()

while True:
    print("\n====== BANK SYSTEM ======")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        bank.create_account()

    elif choice == '2':
        bank.login()

    elif choice == '3':
        print("👋 Thank you for using Bank System.")
        break

    else:
        print("❌ Invalid choice.")