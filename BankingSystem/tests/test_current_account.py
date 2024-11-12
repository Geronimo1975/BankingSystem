from classes.current_account import CurrentAccount
from classes.customer import Customer
import unittest

class TestCurrentAccount(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer(username="testuser", password="hashedpassword", phone="+1234567890", account_type="current")
        self.account = CurrentAccount(account_id="ACC456", owner=self.customer, balance=100)

    def test_deposit(self):
        self.account.deposit(200)
        self.assertEqual(self.account.balance, 300)

    def test_withdraw_within_limit(self):
        self.assertTrue(self.account.withdraw(50))
        self.assertEqual(self.account.balance, 50)

    def test_withdraw_exceeds_limit(self):
        self.assertFalse(self.account.withdraw(200))
