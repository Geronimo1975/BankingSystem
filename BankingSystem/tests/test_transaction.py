import unittest
from classes.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.transaction = Transaction('Deposit', 500.0, 1500.0)
    
    def test_transaction_attributes(self):
        self.assertEqual(self.transaction.transaction_type, 'Deposit')
        self.assertEqual(self.transaction.amount, 500.0)
        self.assertEqual(self.transaction.balance_after, 1500.0)
        self.assertIsNotNone(self.transaction.date)
    
    def test_to_dict(self):
        txn_dict = self.transaction.to_dict()
        self.assertIsInstance(txn_dict, dict)
        self.assertEqual(txn_dict['type'], 'Deposit')
        self.assertEqual(txn_dict['amount'], 500.0)
        self.assertEqual(txn_dict['balance_after'], 1500.0)
        self.assertIn('date', txn_dict)

if __name__ == '__main__':
    unittest.main()
