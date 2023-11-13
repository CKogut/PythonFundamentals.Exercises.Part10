class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class Account:
    def __init__(self, number, type, owner, balance):
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



