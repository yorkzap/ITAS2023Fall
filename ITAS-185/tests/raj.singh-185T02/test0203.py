"""
Course: ITAS 185 - Introduction to Programming
Test02: 03
Description:
    This program defines the `Bread` for inventory of bread with attributes: quantity, type, stock and price
"""

def __init__(self, bread_type='white', quantity=0, price_per_loaf=5.25):
    self.bread_type = bread_type
    self.quantity = quantity
    self.price_per_loaf = price_per_loaf
    
def restock(self, amount):
    self.quantity = self.quantity + amount

def sell(self, amount):
    if amount > self.quantity:
        return -1
    else:
        self.quantity = self.quantity - amount
        return amount * self.price_per_loaf
    
def __str__(self):
    return f"{self.quantity} loaves of {self.bread_type} bread selling at ${self.price_per_loaf:.2f} dollars a loaf."
