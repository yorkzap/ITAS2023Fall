class Account:
    """A simple account class with balance
    """
    def __init__(self, account_type, start_amount=0.0):
        """Initialize the account with the account type and optional amount. Also initialize a list of transactions that is updated whenever a deposit or withdrawal is made 

        Args:
            account_type (string): The account_type of the account
            start_amount (float, optional): The starting amount of the account. Defaults to 0.
        """
        self.account_type = account_type
        self.start_amount = float(start_amount)
        self._transactions = []

    def __getitem__(self, i):
        return self._transactions[i]

    def __len__(self):
        return len(self._transactions)

    def __repr__(self):
        return f'{__class__.__name__}({self.account_type!r}, {self.start_amount!r})'

    def __str__(self):
        return f'{(self.account_type).capitalize()} account started with ${self.start_amount:.2f} and currently has ${self.balance():.2f}'
    
    def balance(self):
        return self.start_amount + sum(self._transactions)
    
    def add_transaction(self, amount):
        """Adds a new transaction to the object

        Args:
            amount (int or float): Amount to be added to the transaction list

        Returns:
            string (optional): Error message if amount is not an int or float
        """
        if not isinstance(amount, (int,float)):
            return 'Please enter and int type for start_amount'
        self._transactions.append(amount)

