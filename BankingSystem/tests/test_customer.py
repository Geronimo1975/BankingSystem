from classes.customer import Customer
import unittest

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer(username="testuser", password="hashedpassword", phone="+1234567890", account_type="saving")

    def test_create_account(self):
        account = self.customer.create_account("saving")
        self.assertEqual(account.owner.username, "testuser")  