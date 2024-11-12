import unittest
from classes.account import Account
from classes.customer import Customer

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(username='testuser', password='hashedpassword', phone='+1234567890', account_type='saving')
        self.account = Account(account_id='ACC123', owner=self.customer, balance=1000.0)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500.0)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 800.0)

    def test_withdraw_insufficient(self):
        self.account.withdraw(1500)
        self.assertEqual(self.account.balance, 1000.0)  

if __name__ == '__main__':
    unittest.main()
