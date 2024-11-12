from cli.menu import BankMenu
from utils.helpers import setup_logging

def main():
    setup_logging()
    bank_menu = BankMenu()
    bank_menu.display_main_menu()

if __name__ == "__main__":
    main()
