from small_town_teller import Person, Account, Bank

zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
alice = Person(2, 'Alice', 'Jones')

zc_bank.add_customer(bob)
zc_bank.add_customer(alice)

bob_savings = Account(1001, "SAVINGS", bob, 200)
alice_savings = Account(1002, "SAVINGS", alice, 450)
zc_bank.add_account(bob_savings)
zc_bank.add_account(alice_savings)



print(zc_bank.balance(1002))
