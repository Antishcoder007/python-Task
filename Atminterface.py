import time

#create a user class
class User:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_pin(self, pin):
        return self.pin == pin

    def add_transaction(self, transaction):
        self.transaction_history.append(transaction)

#create a Account class
class Account:
    def __init__(self, user):
        self.user = user

    def withdraw(self, amount):
        if amount > self.user.balance:
            print("Insufficient funds!")
        else:
            time.sleep(2)
            self.user.balance -= amount
            self.user.add_transaction(f"Withdrawn: ${amount}")
            print(f"${amount} withdrawn successfully.")
            

    def deposit(self, amount):
        time.sleep(3)
        self.user.balance += amount
        self.user.add_transaction(f"Deposited: ${amount}")
        print(f"${amount} deposited successfully.")
        

    def transfer(self, target_user, amount):
        if amount > self.user.balance:
            print("Insufficient funds!")
        else:
            time.sleep(3)
            self.user.balance -= amount
            target_user.balance += amount
            self.user.add_transaction(f"Transferred: ${amount} to User ID {target_user.user_id}")
            target_user.add_transaction(f"Received: ${amount} from User ID {self.user.user_id}")
            print(f"${amount} transferred successfully.")

#create Tracsection History class
class TransactionHistory:
    def __init__(self, user):
        self.user = user

    def display(self):
        if not self.user.transaction_history:
            print("No transactions found.")
        else:
            time.sleep(3)
            print("====================================")
            for transaction in self.user.transaction_history:
                print(transaction)

#create a ATM class
class ATM:
    def __init__(self, bank):
        self.bank = bank
        self.current_user = None

    def authenticate_user(self):
        user_id = input("Enter User ID: ")
        pin = input("Enter PIN: ")
        time.sleep(5)
        user = self.bank.get_user(user_id)
        if user and user.check_pin(pin):
            self.current_user = user
            print("Authentication successful!")
        else:
            print("Authentication failed!")

    def start(self):
        self.authenticate_user()
        if self.current_user:
            self.show_menu()

    def show_menu(self):
        while True:
            time.sleep(1)
            print("====================================")
            print("\n1. Transaction History\n2. Withdraw\n3. Deposit\n4. Transfer\n5. Quit")
            print("\n====================================")
            
            choice = input("Enter your choice: ")
            if choice == '1':
                print("\n====================================")
                history = TransactionHistory(self.current_user)
                history.display()
                print("====================================")
            elif choice == '2':
                print("\n====================================")
                amount = float(input("Enter amount to withdraw: "))
                account = Account(self.current_user)
                account.withdraw(amount)
                print("====================================")
            elif choice == '3':
                print("\n====================================")
                amount = float(input("Enter amount to deposit: "))
                account = Account(self.current_user)
                account.deposit(amount)
                print("====================================")
            elif choice == '4':
                print("\n====================================")
                target_user_id = input("Enter target User ID: ")
                amount = float(input("Enter amount to transfer: "))
                target_user = self.bank.get_user(target_user_id)
                if target_user:
                    account = Account(self.current_user)
                    account.transfer(target_user, amount)
                    print("====================================")
                else:
                    print("Target user not found!")
                    print("====================================")
            elif choice == '5':
                print("Thank you for using our ATM. Goodbye!")
                print("\n==============GOODBYE!!======================")
                break 
            else:
                print("Invalid choice. Please try again.")

# create a Bank class
class Bank:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.user_id] = user

    def get_user(self, user_id):
        return self.users.get(user_id)


# main method
if __name__ == "__main__":
    bank = Bank()
    bank.add_user(User("user1", "user1@123", 1000))
    bank.add_user(User("user2", "user2@123", 500))

    # Create a object of Atm to Access the Start() method
    atm = ATM(bank)
    atm.start()
