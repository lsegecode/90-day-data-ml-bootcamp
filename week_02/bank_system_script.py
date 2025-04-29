# Base Account Class
class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount.")

    def __str__(self):
        return f"Account owner: {self.owner}\nBalance: ${self.balance:.2f}"

# SavingsAccount Class extends Account
class SavingsAccount(Account):
    def __init__(self, owner, balance=0.0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  # 1% by default

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}")

    def __str__(self):
        return (f"Savings Account owner: {self.owner}\n"
                f"Balance: ${self.balance:.2f}\n"
                f"Interest Rate: {self.interest_rate * 100}%")

# Simulating a few transactions
def main():
    print("Welcome to the Bank System!")
    owner_name = input("Enter account owner's name: ")
    initial_balance = float(input("Enter initial balance: "))

    account_type = input("Choose account type (normal/savings): ").strip().lower()

    if account_type == 'savings':
        interest_rate = float(input("Enter interest rate (e.g., 0.02 for 2%): "))
        account = SavingsAccount(owner_name, initial_balance, interest_rate)
    else:
        account = Account(owner_name, initial_balance)

    print("\nAccount created successfully!")
    print(account)

    # Transactions loop
    while True:
        print("\nOptions: deposit, withdraw, interest (savings only), show, exit")
        action = input("What would you like to do? ").strip().lower()

        if action == 'deposit':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif action == 'withdraw':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif action == 'interest':
            if isinstance(account, SavingsAccount):
                account.apply_interest()
            else:
                print("Interest can only be applied to savings accounts.")

        elif action == 'show':
            print(account)

        elif action == 'exit':
            print("Thank you for using the Bank System. Goodbye!")
            break

        else:
            print("Invalid action. Try again.")

if __name__ == "__main__":
    main()
