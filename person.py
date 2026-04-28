# person.py
class Person:
    def __init__(self, name):
        self.name = name
    def add_account(self, account):
        self.account = account
    def __str__(self):
        return f"Name = {self.name}, Number of accounts = {self.account}"