import unittest
import problem1
import numpy as np


class TestProblem1(unittest.TestCase):
    def test_init(self):
        new_account = problem1.Account("John", 0)
        self.assertEqual(new_account.getAccountInfo(), f"John's account (Number: {problem1.bank_of_auvc.num_accounts}) has a balance of $0")

    def test_withdraw(self):
        new_account = problem1.Account("John", 10000)
        new_account.withdraw(10000)
        self.assertEqual(new_account.balance, 0)

        new_account = problem1.Account("Emily", -200)
        self.assertNotEqual(new_account.withdraw(-10000), "Error: Withdrawing more than account balance. ")
        self.assertEqual(new_account.balance, 9800)
        self.assertNotEqual(new_account.balance, -10200)

        new_account = problem1.Account("Serena", 40)
        self.assertEqual(new_account.withdraw(10000), "Error: Withdrawing more than account balance. ")
        self.assertNotEqual(new_account.balance, -9960)
    
    def test_deposit(self):
        new_account = problem1.Account("John", 10000)
        new_account.deposit(10000)
        self.assertEqual(new_account.balance, 20000)

        new_account = problem1.Account("Emily", -200)
        self.assertEqual(new_account.deposit(-10000), "Error: Withdrawing more than account balance. ")
        self.assertNotEqual(new_account.balance, -10200)

        new_account = problem1.Account("Serena", 40)
        new_account.deposit(5)
        self.assertEqual(new_account.balance, 45)
    
    def test_getBalance(self):
        new_account = problem1.Account("John", 10000)
        self.assertEqual(new_account.getBalance(), 10000)

        new_account = problem1.Account("Emily", -200)
        self.assertEqual(new_account.getBalance(), -200)

        new_account = problem1.Account("Serena", 40)
        self.assertEqual(new_account.getBalance(), 40)
    
if __name__ == "__main__":
    unittest.main()