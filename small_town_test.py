from persistent_small_town_teller import Person, Account, Bank

zc_bank = Bank()

# create people
bob = Person(1, 'Bob', 'Smith')
alice = Person(2, 'Alice', 'Jones')

# add to customer list
zc_bank.add_customer(bob)
zc_bank.add_customer(alice)

# verify customers added
print(len(zc_bank.customer_list))

# create and add accounts
bob_savings = Account(1001, "SAVINGS", bob, 200)
alice_savings = Account(1002, "SAVINGS", alice, 450)
zc_bank.add_account(bob_savings)
zc_bank.add_account(alice_savings)

# check Alice's account and make a deposit
print(zc_bank.balance(1002))
zc_bank.deposit(1002, 500.50)
print(zc_bank.balance(1002))

# make withdrawal on Bob's account
zc_bank.withdrawal(1001, 100)
print(zc_bank.balance(1001))

# save data
zc_bank.save_data()

# remove accounts and verify account list empty
zc_bank.remove_account(1001)
zc_bank.remove_account(1002)
print(len(zc_bank.account_list))

# load data
zc_bank.load_data()

# verify accounts have been added back
print(len(zc_bank.account_list))