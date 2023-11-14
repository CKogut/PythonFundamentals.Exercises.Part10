import pickle


class PersistenceUtils:
    @staticmethod
    def file_write(customer_info, acct_info):
        with open('customer_info.pickle', 'wb') as f:
            pickle.dump(customer_info, f)

        with open('acct_info.pickle', 'wb') as f:
            pickle.dump(acct_info, f)

    @staticmethod
    def file_open(file_name):
        with open(file_name, 'rb') as f:
            return pickle.load(f)


class Person:
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


# Declare a Bank class able to support the following operations:
# Adding a customer to the bank
# Adding an account to the bank
# Removing an account from the bank
# Depositing money into an account
# Withdrawing money from an account
# Balance inquiry for a particular account


class Bank:
    def __init__(self):
        self.customer_list = []
        self.account_list = []

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
        for item in self.account_list:
            if item.number == acct_number:
                balance = item.balance
                return balance
        else:
            print('Account not found, no balance to display')

    def save_data(self):
        PersistenceUtils.file_write(self.customer_list, self.account_list)

    def load_data(self):
        self.customer_list = PersistenceUtils.file_open('customer_info.pickle')
        self.customer_list = PersistenceUtils.file_open('acct_info.pickle')

