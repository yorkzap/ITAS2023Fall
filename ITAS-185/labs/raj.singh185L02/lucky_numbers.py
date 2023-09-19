import random

first_name = input('Enter your first name: ')
low = int(input('Enter the lowest number your lucky number can be: '))
high = int(input('Enter the highest number your lucky number can be: '))

lucky_number = random.randint(low, high)
print(f"Hello {first_name}. Your lucky number is {lucky_number}")