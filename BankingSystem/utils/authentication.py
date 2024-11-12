from utils.validation import validate_username, validate_password, validate_phone_number
from classes.customer import Customer
from classes.saving_account import SavingAccount
from classes.current_account import CurrentAccount
from config import CUSTOMERS_FILE, ACCOUNTS_FILE
import json

def login_user(customers_file=CUSTOMERS_FILE, accounts_file=ACCOUNTS_FILE):

    customers = load_customers(customers_file)
    attempts = 0

    while attempts < LOGIN_ATTEMPTS:
        username = input("Te rog să introduci numele de utilizator: ")
        password = getpass.getpass("Te rog să introduci parola: ")

        if username in customers:
            stored_hashed = customers[username]['password'].encode('utf-8')
            if check_password(password, stored_hashed):
                print(f"Welcome back {username}!")
                # Creează un obiect Customer
                account_type = customers[username]['account_type']
                phone = customers[username]['phone']
                customer = Customer(username=username, password=stored_hashed, phone=phone, account_type=account_type)
                
                # Încarcă contul
                account_id = bank.get_account_id(username)
                if account_id and account_id in bank.accounts:
                    if account_type == 'saving':
                        customer.account = SavingAccount(account_id=account_id, owner=customer)
                    elif account_type == 'current':
                        customer.account = CurrentAccount(account_id=account_id, owner=customer)
                    customer.account.load_transactions()
                else:
                    # Dacă nu există cont, creează unul nou
                    customer.account = customer.create_account()
                    self.save_accounts()
                
                return customer
        print("Nume de utilizator sau parolă invalidă.")
        attempts += 1

    print(f"You used {LOGIN_ATTEMPTS} attempts. Please try again after {LOCKOUT_DURATION} seconds.")
    time.sleep(LOCKOUT_DURATION)
    print("Failures reset. Please try again.")
    return None
