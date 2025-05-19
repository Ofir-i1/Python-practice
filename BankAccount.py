from abc import ABC, abstractmethod
import random
import string
from datetime import datetime

#validation funcs
def valid_amount(amount):
    while True:
        try:
            return float(amount)
        except ValueError:
            print("Invalid input.")
            amount = input("Please Enter Valid amount:")

def valid_name(name):
    while not (all(char.isalpha() or char.isspace() for char in name)):
        print("Invalid Name.")
        name=input("Please Enter Valid Name:")
    return name

#abs class
class BankAccount(ABC):
    def __init__(self):
        self.account_num=self.generate_account_num()
        self.owner_name=""
        self.balance=0
        self.log=[]

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    def set_owner_name(self):
        name= input("Hi! Enter your name please: ")
        self.owner_name=valid_name(name)


    def get_account_info(self):
        return {
            "Account Number": self.account_num,
            "Owner": self.owner_name,
            "Balance": self.balance
        }


    def set_log(self,action, amount_or_rate):
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        if action == "withdraw" or action == "deposit":
            entry = (
                f"{now}\n"
                f"{action} "
                f"of:{amount_or_rate}\n"
                f"new balance after {action}: {self.balance}\n"
             )
            self.log.append(entry)
        elif action == "set_interest_rate" or action =="autoRateToBalance":
            entry = (
                f"{now}\n"
                f"{action} "
                f"of:{amount_or_rate}\n"
                f"new balance after {action}: {self.balance}\n"
            )
            self.log.append(entry)

    #func generate one time rand acc num
    def generate_account_num(self):
        characters = string.ascii_letters + string.digits
        acc_num = ''.join(random.choice(characters) for _ in range(6))
        return acc_num





class CheckingAccount(BankAccount):

    def __init__(self):
        super().__init__()

    def withdraw(self, amount):
        amount= valid_amount(amount)
        if amount > self.balance:
            print("You don't have enough money!")
        else:
            self.balance -= amount
            self.set_log("withdraw", amount)

    def deposit(self, amount):
        amount = valid_amount(amount)
        self.balance+=amount
        self.set_log("deposit", amount)

    def get_balance(self):
        return self.balance

    #to string
    def __str__(self):
        info = self.get_account_info()
        return f"Account Number: {info['Account Number']}, Owner: {info['Owner']}, Balance: {info['Balance']}"



class SavingAccount(BankAccount):

    def __init__(self, interest_rate ):
        super().__init__()
        self.interest_rate=interest_rate

    def withdraw(self, amount):
        amount = valid_amount(amount)
        if amount > self.balance:
            print("You don't have enough money!")
        else:
            self.balance -= amount
            self.set_log("withdraw", amount)

    def deposit(self, amount):
        amount = valid_amount(amount)
        self.balance+=amount
        self.set_log("deposit", amount)

    def get_interest_rate(self):
        print(f"The interest rate of this account: {self.interest_rate}")
        return self.interest_rate

    def set_interest_rate(self,rate):
        rate = valid_amount(rate)
        self.interest_rate=rate
        self.apply_interest_to_balance() #with new rate
        self.set_log("set_interest_rate", self.interest_rate)

    def apply_interest_to_balance(self):
        self.balance += self.balance * self.interest_rate
        self.set_log("autoRateToBalance", self.interest_rate)

    def get_balance(self):
        return self.balance

    # to string
    def __str__(self):
        info = self.get_account_info()
        return f"Account Number: {info['Account Number']}, Owner: {info['Owner']}, Balance: {info['Balance']}, Interest rate: {self.interest_rate}"


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account: BankAccount):
        self.accounts[account.account_num] = account

    def get_account(self, account_num):
        account = self.accounts.get(account_num)
        if account:
            return account
        else:
            print("There is no account by this number.")
            return None

    def deposit_to_account(self, account_num, amount):
        account = self.get_account(account_num)
        if account:
            account.deposit(amount)


    def withdraw_from_account(self, account_num, amount):
        account = self.get_account(account_num)
        if account:
            account.withdraw(amount)

    def print_account_log(self, account_num):
        account = self.get_account(account_num)
        if account:
            for entry in account.log:
                print(entry)

    def print_all_accounts(self):
        for acc in self.accounts.values():
            print(acc)


def main():
    print("Running test scenario...\n")
    bank = BankSystem()

    # Checking Account
    checking = CheckingAccount()
    checking.set_owner_name()
    checking.deposit(500)
    checking.withdraw(200)
    bank.add_account(checking)

    # Saving Account
    saving = SavingAccount(0.05)
    saving.set_owner_name()
    saving.deposit(1000)
    saving.set_interest_rate(0.04)
    saving.apply_interest_to_balance()
    saving.withdraw(300)
    bank.add_account(saving)

    # Print individual accounts
    print("\n--- Account Info ---")
    print(checking)
    print(saving)

    # Print logs
    print("\n--- Logs ---")
    print("Checking Log:")
    bank.print_account_log(checking.account_num)

    print("Saving Log:")
    bank.print_account_log(saving.account_num)

    # Write to file
    print("\n--- Writing logs to files ---")
    for acc in [checking, saving]:
        with open(f"log_{acc.account_num}.txt", "w") as f:
            for entry in acc.log:
                f.write(entry + "\n")
        print(f"log_{acc.account_num}.txt written.")

    # Show all accounts
    print("\n--- All Accounts ---")
    bank.print_all_accounts()


#menu func
def bank_menu():
    bank = BankSystem()

    while True:
        print("\n--- Welcome to the Bank System ---")
        print("1. Create Checking Account")
        print("2. Create Saving Account")
        print("3. Deposit to Account")
        print("4. Withdraw from Account")
        print("5. Show Account Info")
        print("6. Show Account Log")
        print("7. Print Account Log to File")
        print("8. Show All Accounts")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        if choice == '1':
            acc = CheckingAccount()
            acc.set_owner_name()
            bank.add_account(acc)
            print("Checking account created successfully. Account Number:", acc.account_num)

        elif choice == '2':
            rate = input("Enter interest rate (e.g., 0.03): ")
            acc = SavingAccount(valid_amount(rate))
            acc.set_owner_name()
            bank.add_account(acc)
            print("Saving account created successfully. Account Number:", acc.account_num)

        elif choice == '3':
            acc_num = input("Enter account number: ")
            amount = input("Enter amount to deposit: ")
            bank.deposit_to_account(acc_num, amount)

        elif choice == '4':
            acc_num = input("Enter account number: ")
            amount = input("Enter amount to withdraw: ")
            bank.withdraw_from_account(acc_num, amount)

        elif choice == '5':
            acc_num = input("Enter account number: ")
            acc = bank.get_account(acc_num)
            if acc:
                print(acc)

        elif choice == '6':
            acc_num = input("Enter account number: ")
            bank.print_account_log(acc_num)

        elif choice == '7':
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                with open(f"log_{acc_num}.txt", "w") as f:
                    for entry in account.log:
                        f.write(entry + "\n")
                print(f"Log written to log_{acc_num}.txt")

        elif choice == '8':
            bank.print_all_accounts()

        elif choice == '9':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    bank_menu()








