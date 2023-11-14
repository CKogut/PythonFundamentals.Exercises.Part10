class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class Account:
    def __init__(self, number, type, owner, balance=0):
        self.number = number
        self.type = type
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
        if person in self.customer_list:
            print("Already a customer")
        else:
            self.customer_list.append(person)

    def add_account(self, account):
        self.account_list.append(account)

    def remove_account(self, account):
        self.account.remove(account)

    def deposit(self, account):
        pass

    def withdrawal(self, account):
        pass

    def balance(self, number):
        # iterate through account list, find matching account number, return the balance
        balance = [item.balance for item in self.account_list if item.number == number]
        return balance
