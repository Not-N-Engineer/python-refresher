import numpy as np

class Bank:
    def __init__(self):
        self.num_accounts = 0

bank_of_auvc = Bank()


class Account:
    def __init__(self, name, starting_balance):
        bank_of_auvc.num_accounts += 1
        self.name = name
        self.balance = starting_balance
        self.account_num = bank_of_auvc.num_accounts
    
    def check_for_overdraft(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError
        if self.balance + amount < 0:
            print("Error: Withdrawing more than account balance. ")
            return False # should not go through with transaction
        else:
            return True 

    def withdraw(self, amount):
        if self.check_for_overdraft(-amount):
            self.balance -= amount
        else:
            return "Error: Withdrawing more than account balance. "
    
    def deposit(self, amount):
        if self.check_for_overdraft(amount):
            self.balance += amount
        else:
            return "Error: Withdrawing more than account balance. "

    def getBalance(self):
        return self.balance
    
    def getAccountInfo(self):
        return f"{self.name}'s account (Number: {self.account_num}) has a balance of ${self.balance}"

    def __str__(self):
        return f"{self.name}'s account (Number: {self.account_num}) has a balance of ${self.balance}"