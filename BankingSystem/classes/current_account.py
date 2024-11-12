from classes.account import Account
from config import OVERDRAFT_LIMIT

class CurrentAccount(Account):

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.record_transaction('Withdrawal', amount)
            print(f"Successful withdrawal! The actual balance is: {self.balance:.2f} EUR")
            return True
        else:
            print("Insufficient funds or invalid amount.")
            return False
