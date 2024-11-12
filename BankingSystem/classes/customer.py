from classes.current_account import CurrentAccount
from classes.saving_account import SavingAccount  # Ensure this import exists

class Customer:
    def __init__(self, username, password, phone, account_type):
        self.username = username
        self.password = password
        self.phone = phone
        self.account_type = account_type
        self.account = self.create_account(account_type)  
    
    def create_account(self, account_type):
        if account_type == "saving":
            return SavingAccount(account_id="ACC789", owner=self, balance=0)
        elif account_type == "current":
            return CurrentAccount(account_id="ACC123", owner=self, balance=0)
        else:
            raise ValueError("Invalid account type")


    def set_account(self, account):
        self.account = account