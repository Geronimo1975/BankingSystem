from classes.bank import Bank

class Bank(object):
    
    def __init__(self):
       
        self.customers = {}

    def create_user(self, username, password, phone, account_type):
      
        if username in self.customers:
            return False
        
      
        self.customers[username] = {
            "username": username,
            "password": password,
            "phone": phone,
            "account_type": account_type,
            "balance": 0  
        return True

    def authenticate_user(self, username, password):
  
        user = self.customers.get(username)
        if user and user["password"] == password:
            return user
        return None


class BankMenu:
    def __init__(self):
        self.bank = Bank()

    def display_main_menu(self):
        pass

    def display_user_menu(self, user):
        pass
            
    def register_user(self):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        phone = input("Please enter your phone number: ")
        account_type = input("Choose account type (saving/current): ")

  
        if self.bank.create_user(username, password, phone, account_type):
            print(f"Registration successful for {username}")
        else:
            print("Username already exists, please try another one.")

    def login_user(self):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")


        user = self.bank.authenticate_user(username, password)
        if user:
            print(f"Welcome back {username}!")
            return user
        else:
            print("Invalid username or password.")
            return None



if __name__ == "__main__":
    menu = BankMenu()
    
    print("===== Register User =====")
    menu.register_user()  
    print("\n===== Login User =====")
    menu.login_user()  