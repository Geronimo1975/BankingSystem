###Banking System

This project is a Python-based Banking System application that simulates essential banking operations, including account creation, deposits, withdrawals, transaction history tracking, and more. This system is designed to manage multiple types of accounts (e.g., savings, current) and keep a detailed record of all transactions made by customers.

##Features

#Account Creation: 
Supports creating different types of accounts (e.g., savings and current) with unique IDs.
#Deposit and Withdrawal: 
Allows users to deposit and withdraw funds with appropriate checks for balance sufficiency and transaction limits.
#Transaction History: 
Maintains a log of each account's transactions, recording details such as type, amount, balance after each transaction, and timestamp.
#Statement Generation: 
Generates and displays account statements, summarizing all transactions made by the account holder.
#Data Persistence: 
Saves transaction histories to a file, allowing the system to persist data across sessions.
#Testing Suite: 
Includes unit tests to ensure each function behaves as expected, helping to verify the correctness of core functionalities.

##File Structure

classes/
#account.py: 
Defines the base Account class with core functionalities, such as deposit, withdrawal, and transaction recording.
#current_account.py: 
Defines the CurrentAccount class, inheriting from Account with features specific to current accounts.
#saving_account.py: 
Defines the SavingAccount class, inheriting from Account with features specific to savings accounts.
#customer.py: 
Defines the Customer class for managing customer details and linking them to their respective accounts.
#transaction.py: 
Defines the Transaction class, encapsulating details of individual transactions.
#tests/: 
Contains unit tests to validate the functionality of the system, ensuring each module behaves as expected.

#config.py: 
Holds configuration constants, such as the file path for saving transaction history (ACCOUNTS_FILE) and other constants like INTEREST_RATE.

#data/: 
Contains persistent data files used by the application (e.g., accounts file for storing transaction history).

##Requirements

This project is built using Python 3.12 and requires the following libraries:

json: for data storage
datetime: for handling transaction timestamps
unittest: for running unit tests
