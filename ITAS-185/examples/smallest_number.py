# use a pseudocode to write an algorithm to find the smallest number in a list of numbers
# List of numbers
numbers = [1, 3, 5, 7, 0]
# Initialize the smallest number
smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number
        
print(f"the smallest number so far is {smallest}")

