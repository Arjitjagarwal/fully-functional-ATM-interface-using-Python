class Account:
    def _init_(self, card_number, pin, balance=0.0):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited ₹{amount:.2f}")
            print(f"₹{amount:.2f} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            self.history.append(f"Withdrew ₹{amount:.2f}")
            print(f"₹{amount:.2f} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance:.2f}")

    def show_history(self):
        print("Transaction History:")
        if not self.history:
            print("No transactions yet.")
        else:
            for h in self.history:
                print(" -", h)

# Sample user database
accounts = {
    "1111": Account("1111", "1234", 5000),
    "2222": Account("2222", "4321", 10000)
}

def authenticate(card_number, pin):
    account = accounts.get(card_number)
    if account and account.pin == pin:
        return account
    return None

def atm_menu(account):
    while True:
        print("\n==== ATM Menu ====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            account.check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: ₹"))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: ₹"))
            account.withdraw(amount)
        elif choice == '4':
            account.show_history()
        elif choice == '5':
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid option, try again.")

def main():
    print("==== Welcome to Python ATM ====")
    card_number = input("Enter your card number: ")
    pin = input("Enter your PIN: ")

    user_account = authenticate(card_number, pin)
    if user_account:
        atm_menu(user_account)
    else:
        print("Authentication failed. Please check your card number or PIN.")

if _name_ == "_main_":
    main()
