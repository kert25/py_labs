import unittest


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount


class TestBankAccount(unittest.TestCase):
    def test_initial_balance(self):
        account = BankAccount(100)
        self.assertEqual(account.balance, 100)

    def test_deposit(self):
        account = BankAccount()
        account.deposit(50)
        self.assertEqual(account.balance, 50)

    def test_withdraw(self):
        account = BankAccount(100)
        account.withdraw(30)
        self.assertEqual(account.balance, 70)

    def test_withdraw_insufficient(self):
        account = BankAccount(50)
        with self.assertRaises(ValueError):
            account.withdraw(100)

    def test_deposit_negative(self):
        account = BankAccount()
        with self.assertRaises(ValueError):
            account.deposit(-10)


unittest.main()
