import json
from datetime import datetime
from config import ACCOUNTS_FILE

class Account:

    def __init__(self, account_id, owner, balance=0.0):
        self.account_id = account_id
        self.owner = owner  
        self.balance = balance
        self.transaction_history = []


        if not hasattr(self.owner, 'username'):
            raise AttributeError("The Owner must be a Customer instance and have the `username` attribute.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.record_transaction('Deposit', amount)
            print(f"Successful deposit! New balance: {self.balance:.2f} EUR")
        else:
            print("The deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.record_transaction('Withdrawal', amount)
            print(f"Successful withdrawal! New balance is: {self.balance:.2f} EUR")
            return True
        else:
            print("Insufficient funds or invalid amount.")
            return False

    def record_transaction(self, transaction_type, amount):
        transaction = {
            'type': transaction_type,
            'amount': amount,
            'balance_after': self.balance,
            'date': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        self.transaction_history.append(transaction)
        self.save_transactions()

    def generate_statement(self):
        print(f"\nAccount statement for {self.owner.username}")
        print("---------------------------")
        for txn in self.transaction_history:
            print(f"{txn['type']}: {txn['amount']:.2f} EUR, Balance after: {txn['balance_after']:.2f} EUR on {txn['date']}")
        print()

    def save_transactions(self):
        account_data = {
            'account_id': self.account_id,
            'owner': self.owner.username,  
            'balance': self.balance,
            'transaction_history': self.transaction_history
        }
        try:
            with open(ACCOUNTS_FILE, 'r') as file:
                accounts = json.load(file)
        except FileNotFoundError:
            accounts = {}

        accounts[self.account_id] = account_data

        with open(ACCOUNTS_FILE, 'w') as file:
            json.dump(accounts, file, indent=4)

    def load_transactions(self):
        try:
            with open(ACCOUNTS_FILE, 'r') as file:
                accounts = json.load(file)
            account_data = accounts.get(self.account_id, {})
            self.balance = account_data.get('balance', 0.0)
            self.transaction_history = account_data.get('transaction_history', [])
        except FileNotFoundError:
            self.balance = 0.0
            self.transaction_history = []

    def to_dict(self):
        return {
            'account_id': self.account_id,
            'owner': self.owner.username, 
            'balance': self.balance,
            'transaction_history': self.transaction_history
        }
