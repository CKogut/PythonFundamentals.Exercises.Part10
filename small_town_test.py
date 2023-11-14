from small_town_teller import Person, Account, Bank

zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
alice = Person(2, 'Alice', 'Jones')
alice2 = Person(3, 'Alice', 'Jones')

zc_bank.add_customer(bob)
zc_bank.add_customer(alice)
zc_bank.add_customer(alice2)
zc_bank.add_customer(alice2)

bob_savings = Account(1001, "SAVINGS", bob, 200)
alice_savings = Account(1002, "SAVINGS", alice, 450)
zc_bank.add_account(bob_savings)
zc_bank.add_account(alice_savings)

print(zc_bank.balance(1002))
zc_bank.deposit(1002, 500)
print(zc_bank.balance(1002))

zc_bank.withdrawal(1001, 100)
print(zc_bank.balance(1001))




