class SavingAccount:
    def __init__(self, account_id, owner, balance=0):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):

        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
    
        self.balance += amount
