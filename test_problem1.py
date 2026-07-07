import unittest
import problem1
import numpy as np
import pytest


class TestProblem1(unittest.TestCase):
    def test_init(self):
        new_account = problem1.BankAccount("John", 0)
        assert new_account == new_account

    def test_withdraw(self):
        new_account = problem1.BankAccount("John", 10000)
        new_account.withdraw(10000)
        assert new_account.balance == 0

        new_account = problem1.BankAccount("Emily", -200)
        new_account.withdraw(-10000)
        assert new_account.balance == 9800

        new_account = problem1.BankAccount("Serena", 40)
        new_account.withdraw(10000)
        assert new_account.balance == -9960
    
    def test_deposit(self):
        new_account = problem1.BankAccount("John", 10000)
        new_account.deposit(10000)
        assert new_account.balance == 20000

        new_account = problem1.BankAccount("Emily", -200)
        new_account.deposit(-10000)
        assert new_account.balance == -10200

        new_account = problem1.BankAccount("Serena", 40)
        new_account.deposit(5)
        assert new_account.balance == 45
    
    def test_printBalance(self):
        new_account = problem1.BankAccount("John", 10000)
        assert new_account.printBalance() == 10000

        new_account = problem1.BankAccount("Emily", -200)
        assert new_account.printBalance() == -200

        new_account = problem1.BankAccount("Serena", 40)
        assert new_account.printBalance() == 40
    
if __name__ == "__main__":
    unittest.main()