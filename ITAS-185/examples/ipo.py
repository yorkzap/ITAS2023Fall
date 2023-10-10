# Write an IPO diagram for a program to compute total cost after the sales tax for a purchase. 
# Assume that the sales tax rate is a constant.
# The purchase amount should be input from the user.


# input = purchase price
# sales Tax Rate (constant)
# process = calculate total cost (Purchase Amount + Sales Tax)
# output =  - Total Cost (after adding sales tax)

purchase_price = float(input("Enter the purchase price "))
sales_tax_rate = .05

total_cost = (purchase_price + (purchase_price * sales_tax_rate))

print(total_cost)