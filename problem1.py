import numpy as np

class BankAccount:
    num_accounts = 0

    def __init__(self, name, starting_balance):
        BankAccount.num_accounts += 1
        self.name = name
        self.balance = starting_balance
        self.account_num = BankAccount.num_accounts
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount
    
    def printBalance(self):
        print(self.balance)
        return self.balance