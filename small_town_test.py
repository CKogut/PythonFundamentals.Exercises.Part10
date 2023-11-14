from persistent_small_town_teller import Person, Account, Bank

zc_bank = Bank()

bob = Person(1, 'Bob', 'Smith')
alice = Person(2, 'Alice', 'Jones')

zc_bank.add_customer(bob)
zc_bank.add_customer(alice)

print(len(zc_bank.customer_list))

bob_savings = Account(1001, "SAVINGS", bob, 200)
alice_savings = Account(1002, "SAVINGS", alice, 450)
zc_bank.add_account(bob_savings)
zc_bank.add_account(alice_savings)
zc_bank.add_account(alice_savings)

print(zc_bank.balance(1002))
zc_bank.deposit(1002, 500.50)
print(zc_bank.balance(1002))

zc_bank.withdrawal(1001, 100)
print(zc_bank.balance(1001))

zc_bank.remove_account(1001)
print(zc_bank.balance(1001))

zc_bank.deposit(1003, 500)

zc_bank.save_data()
