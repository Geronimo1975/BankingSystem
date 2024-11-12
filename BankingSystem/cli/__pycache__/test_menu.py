import unittest
from cli.menu import BankMenu

class TestBankMenu(unittest.TestCase):

    def setUp(self):
        # Aceasta va fi apelată înainte de fiecare test
        self.menu = BankMenu()

    def test_register_user(self):
        # Testăm înregistrarea unui utilizator nou
        self.assertTrue(self.menu.bank.create_user("testuser", "password123", "+491234567890", "saving"))
        # Testăm înregistrarea cu un username existent
        self.assertFalse(self.menu.bank.create_user("testuser", "password123", "+491234567890", "saving"))

    def test_authenticate_user(self):
        # Înregistrăm un utilizator pentru a testa autentificarea
        self.menu.bank.create_user("testuser", "password123", "+491234567890", "saving")
        # Testăm autentificarea corectă
        user = self.menu.bank.authenticate_user("testuser", "password123")
        self.assertIsNotNone(user)
        # Testăm autentificarea cu parola greșită
        user = self.menu.bank.authenticate_user("testuser", "wrongpassword")
        self.assertIsNone(user)

if __name__ == "__main__":
    unittest.main()
