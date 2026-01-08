class BankAccount:
    def _init_(self):
        self.balance = 0.0
        print("Welcome to the Simple Bank!")

    def deposit(self):
        amount = 1000 
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}\n")
        else:
            print("Deposit amount must be positive.\n")

    def withdraw(self):
        amount = 500 
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}\n")
            else:
                print("Insufficient balance.\n")
        else:
            print("Withdrawal amount must be positive.\n")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}\n")
# --- Main Program ---
if _name_ == "_main_":
    account = BankAccount()
    account.deposit()
    account.withdraw()
    account.display_balance()
