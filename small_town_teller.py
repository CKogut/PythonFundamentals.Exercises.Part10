class Person:
    next_id = 1

    def __init__(self, p_id, first_name, last_name):
        self.p_id = p_id
        self.first_name = first_name
        self.last_name = last_name



class Account:
    def __init__(self, number, acct_type, owner, balance=0.0):
        self.number = number
        self.type = acct_type
        self.owner = owner
        self.balance = balance


""" 
Declare a Bank class able to support the following operations:
Adding a customer to the bank
Adding an account to the bank
Removing an account from the bank
Depositing money into an account
Withdrawing money from an account
Balance inquiry for a particular account
"""


class Bank:
    def __init__(self):
        self.account_list = []
        self.customer_list = []

    def add_customer(self, person: Person) -> None:
        for item in self.customer_list:
            if item.p_id == person.p_id:
                print("Customer ID already exists")
                break
        else:
            self.customer_list.append(person)

    def add_account(self, account: Account) -> None:
        for item in self.account_list:
            if item.number == account.number:
                print("Account number already exists")
                break
        else:
            self.account_list.append(account)

    def remove_account(self, number: int) -> None:
        for item in self.account_list:
            if item.number == number:
                self.account_list.remove(item)
                break
        else:
            print('Account not found, unable to delete')

    def deposit(self, acct_number: int, amount: float) -> None:
        for item in self.account_list:
            if item.number == acct_number:
                item.balance += amount
                break
        else:
            print('Account not found, no deposit made')

    def withdrawal(self, acct_number: int, amount: float) -> None:
        for item in self.account_list:
            if item.number == acct_number:
                item.balance -= amount
                break
        else:
            print('Account not found, no withdrawal made')

    def balance(self, acct_number: int) -> float:
        # iterate through account list, find matching account number, return the balance
        balance = [item.balance for item in self.account_list if item.number == acct_number]
        return balance
