class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

class ATM:
    def __init__(self):
        self.users = {}  # Store user data (user_id: User)
        self.current_user = None

    def create_user(self, user_id, pin):
        new_user = User(user_id, pin)
        self.users[user_id] = new_user

    def login(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            self.current_user = self.users[user_id]
            return True
        else:
            return False

    def display_menu(self):
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def perform_transaction(self, choice):
        if choice == 1:
            self.display_transaction_history()
        elif choice == 2:
            amount = float(input("Enter the amount to withdraw: "))
            self.withdraw(amount)
        elif choice == 3:
            amount = float(input("Enter the amount to deposit: "))
            self.deposit(amount)
        elif choice == 4:
            recipient_id = input("Enter the recipient's user ID: ")
            amount = float(input("Enter the amount to transfer: "))
            self.transfer(recipient_id, amount)

    def display_transaction_history(self):
        print("Transaction History:")
        for transaction in self.current_user.transaction_history:
            print(transaction)

    def withdraw(self, amount):
        if amount > 0 and amount <= self.current_user.balance:
            self.current_user.balance -= amount
            self.current_user.transaction_history.append(f"Withdraw: ${amount}")
            print(f"Withdrawal successful. Current balance: ${self.current_user.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def deposit(self, amount):
        if amount > 0:
            self.current_user.balance += amount
            self.current_user.transaction_history.append(f"Deposit: ${amount}")
            print(f"Deposit successful. Current balance: ${self.current_user.balance}")
        else:
            print("Invalid deposit amount.")

    def transfer(self, recipient_id, amount):
        if recipient_id in self.users and amount > 0 and amount <= self.current_user.balance:
            recipient = self.users[recipient_id]
            self.current_user.balance -= amount
            recipient.balance += amount
            self.current_user.transaction_history.append(f"Transfer to {recipient_id}: ${amount}")
            recipient.transaction_history.append(f"Transfer from {self.current_user.user_id}: ${amount}")
            print(f"Transfer successful. Current balance: ${self.current_user.balance}")
        else:
            print("Invalid transfer or insufficient funds.")
            
    def run(self):
        print("Welcome to the ATM system!")
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")

        if self.login(user_id, pin):
            while True:
                self.display_menu()
                choice = int(input("Enter your choice (1-5): "))

                if choice == 5:
                    print("Thank you for using the ATM. Goodbye!")
                    break

                self.perform_transaction(choice)
        else:
            print("Invalid user ID or PIN. Exiting...")

# Example usage:
atm = ATM()
atm.create_user("12345", "6789")  # Replace with actual user data
atm.create_user("67890", "1234")  # Replace with actual user data
atm.create_user("54321", "5678")  # Replace with actual user data
atm.create_user("98765", "4321")  # Replace with actual user data
atm.run()
