"""
Course: ITAS 185 - Introduction to Programming
Test03: 02 (Account Class)
Description:
    This is the Account class, representing a bank account with an owner, starting amount, 
    and a list of transactions. It allows addition of transactions, calculates the 
    current balance, and prints account details. The Account class also includes
    try and exception statements to handle errors.
"""

class Account:
    def __init__(self, owner="", start_amount=0):
        try:
            if owner == "":
                raise ValueError("Owner cannot be empty")
            self.owner = owner

            if type(start_amount) is not int or start_amount < 0:
                raise ValueError(f"Amount must be a positive integer, {start_amount} received")
            self.start_amount = start_amount

        except ValueError as e:
            raise TypeError("*#*ERROR*#+ " + str(e))

        self._transactions = []

    def add_transaction(self, amount):
        if type(amount) is not int:
            raise ValueError("*#+ERROR**» Please enter an integer amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.start_amount + sum(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount {self.start_amount}"

    def __len__(self):
        return len(self._transactions)
