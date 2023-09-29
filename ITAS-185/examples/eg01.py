from colorama import Fore, Back, Style

num_list = [3, 4, 5, 6, 7]

# Set the text color to green
print(Fore.GREEN + "Numbers in the list:")

# Print each number with green text color

# Reset the text color to the default
print(f"{Fore.CYAN}{Back.BLACK}{num_list[-2]}")

list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['X', 'Y', 'Z']
list1[2:4] = list2

num_list.append(42) 

a1 = [1, 2, 3]
b1 = a1
