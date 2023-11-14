import persistence_utils


class Person:
    next_id = 1

    def __init__(self, first_name, last_name):
        self.id = self.next_id
        self.first_name = first_name
        self.last_name = last_name
        self.next_id += 1


class Account:
    def __init__(self, number, acct_type, owner, balance=0):
        self.number = number
        self.acct_type = acct_type
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

    def add_customer(self, person):
        match = False

        for item in self.customer_list:
            if item.p_id == person.p_id:
                match = True
                print("Customer ID already exists")
                break

        if not match:
            self.customer_list.append(person)

    def add_account(self, account):
        match = False

        for item in self.account_list:
            if item.number == account.number:
                match = True
                print("Account number already exists")
                break

        if not match:
            self.account_list.append(account)

    def remove_account(self, account):
        self.account_list.remove(account)

    def deposit(self, acct_number, amount):
        for item in self.account_list:
            if item.number == acct_number:
                item.balance += amount

    def withdrawal(self, acct_number, amount):
        for item in self.account_list:
            if item.number == acct_number:
                item.balance -= amount

    def balance(self, acct_number):
        # iterate through account list, find matching account number, return the balance
        balance = [item.balance for item in self.account_list if item.number == acct_number]
        return balance


class PersistenceUtils:

    def write_pickle(self, file_path, data):
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)

    def load_pickle(file_path):
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
        return data
