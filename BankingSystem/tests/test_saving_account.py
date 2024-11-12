import unittest
from classes.customer import Customer
from config import INTEREST_RATE

class TestSavingAccount(unittest.TestCase):
    def setUp(self):
        from classes.saving_account import SavingAccount  
        self.customer = Customer(
            username="testuser",
            password="hashedpassword",
            phone="+1234567890",
            account_type="saving"  
        )
        
        self.account = self.customer.create_account("saving")

    def test_deposit_with_interest(self):
        initial_balance = self.account.balance
        self.account.deposit(500)
        self.assertEqual(self.account.balance, initial_balance + 500)

if __name__ == "__main__":
    unittest.main()
