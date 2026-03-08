from account import Account
from bank import Bank

bank = Bank()

bank.add_account(Account(1000001, 5000.0, 5.0))
bank.add_account(Account(1000002, 10000.0, 7.5))

print("Initial accounts:")
bank.print_all_accounts()

account1 = bank.get_account_by_number(1000001)
if account1:
    print(f"\nBalance before operations: {account1.get_balance()}")
    account1.deposit(2000)
    print(f"Balance after deposit: {account1.get_balance()}")
    account1.withdraw(1000)
    print(f"Balance after withdrawal: {account1.get_balance()}")
    interest = account1.calculate_interest()
    print(f"Calculated interest: {interest}")

print("\nFinal accounts:")
bank.print_all_accounts()