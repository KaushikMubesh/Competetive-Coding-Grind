class BankAccount{
    def __init__(self,AccNumber,Password,UserName,Balance = 0){
        self.AccNumber = AccNumber
        self.Password = Password
        self.UserName = UserName
        self.Balance = Balance
    }
    def Deposite(self,amount):
        if (amount>0):
            self.Balance+=amount
        else:
            print("Invalid Amount")
    def Withdraw(self,Amount):
        if(amount>=self.Balance):
            self.Balance-=Amount
        else:
            print("Not enough Money to withdraw !!")
    def CheckBalance(self,Amount):
        print("Current Balance is : " , self.Balance)
    
    def DetailsCheck():
        print("User Name : " ,self.UserName)
        print("Acc No : ",self.AccNumber)
        print("Balance : " , self.Balance)

        
class Bank:

    def __init__(self):
        self.Accounts = {}
    def CreateAccount (self):
        b=0
        while(b==0):
            Userid = int(input("Enter ur User id"))
            if (userid in self.Accounts):
                Print("User Id already Taken ")
                continue
            b=1
        username = input("Enter the User Name ")
        password = input("Enter the password ")
        Balance = int(input("Enter the amount to be deposited First !! "))
        save = BankAccount(userid,password,username,balance)
        self.account[userid]  = save
    
    def Login_account(self):
        accno = int(input("Enter the acount Number "))
        password = input()
        x=self.Accounts[accno]
        if x and x.password==password:
            print("Login Succesful !!")
        else:
            print("Wrong Accno or password ")

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
                account.Deposite(amount)

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

}