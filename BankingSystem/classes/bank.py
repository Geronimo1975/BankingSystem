from classes.account import Account 
from classes.customer import Customer
import json

class Bank:
    def __init__(self):
    
        self.customers = {} 
        self.accounts = {} 
    def create_user(self, username, password, phone, account_type):
        
        if username in self.customers:
            print("Username already exists.")
            return False

        
        new_customer = Customer(username, password, phone, account_type)
        self.customers[username] = new_customer
        self.accounts[new_customer.account.account_id] = new_customer.account
        print(f"Account created for {username}")
        return True

    def authenticate_user(self, username, password):
        
        customer = self.customers.get(username)
        if customer and customer.password == password:
            return customer
        print("Invalid username or password.")
        return None

    def transfer_funds(self, sender_username, recipie
 
        if sender_username not in self.customers:
            print("Sender not found.")
            return False
        if recipient_username not in self.customers:
            print("Recipient not found.")
            return False

        sender = self.customers[sender_username]
        recipient = self.customers[recipient_username]

    
        if sender.account.balance < amount:
            print("Insufficient funds.")
            return False

        sender.account.balance -= amount
        recipient.account.balance += amount
        print(f"Transfer successful! {amount} EUR transferred from {sender_username} to {recipient_username}.")
        return True


class DataManager:
    def __init__(self, accounts_file='data/accounts.json', customers_file='data/customers.json'):
        self.accounts_file = accounts_file
        self.customers_file = customers_file

    def load_accounts(self):
        with open(self.accounts_file, 'r') as f:
            return json.load(f)

    def save_accounts(self, accounts_data):
        with open(self.accounts_file, 'w') as f:
            json.dump(accounts_data, f, indent=4)

    def load_customers(self):
        with open(self.customers_file, 'r') as f:
            return json.load(f)

    def save_customers(self, customers_data):
        with open(self.customers_file, 'w') as f:
            json.dump(customers_data, f, indent=4)
