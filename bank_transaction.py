
user_logged_in = False
from random import randint


class Bank_Account:

    def __init__(self, name, balance = 0):

        self._balance_amount = balance
        self._name = name
        self._account_number = randint(1000000000, 9999999999)
            

    def deposit(self, amount):
        self._balance_amount += amount
        return self._balance_amount

    def withdraw(self, amount):

        if self._balance_amount >= amount:
            self._balance_amount -= amount
            return self._balance_amount
        else:
            raise ValueError("\nYou don't have enough balance to withdraw")

    @property
    def balance(self):
        return self._balance_amount 
    

