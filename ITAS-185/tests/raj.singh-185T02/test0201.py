"""
Course: ITAS 185 - Introduction to Programming
Test02: 01
Description:
    Several functions demonstrating list comprehensions
"""

def cubed(max_num):
    """
    Return a list which contains the cube of all the numbers that are evenly 
    divisible by three from 1 up to and including max_num.
    """
    return [i**3 for i in range(1, max_num + 1) if i % 3 == 0]

def num_str(lower_num, upper_num):
    """
    Return a dictionary that contains the number as the key and the 
    string value of the number as the value for each value passed
    """
    return {num: str(num) for num in range(lower_num, upper_num + 1)}

def common_num(list_a, list_b):
    """
    Return a dictionary that contains the number as the key and the
    string value of the number as the value for each value passed
    """
    return [num for num in list_a if num not in list_b]

def short_words(the_string):
    """
    Return a list of the words that are less than 5 characters long or an empty list if there are none
    """
    # Divide the string into words
    words = the_string.split()
    # Create a list of words that are less than five in length
    return [word for word in words if len(word) < 5]


if __name__ == "__main__":
    # Cubed function testing
    print("cubed() test")
    print("Case 1: Cube of 5 - Expected: [27], Result -", cubed(5))
    print("Case 2: Cube of 6 - Expected: [27, 216], Result -", cubed(6))
    print("Case 3: Cube of 16 - Expected: [27, 216, 729, 1728, 3375], Result- ", cubed(16))
    print(f"{'-' * 50}\n")


    # num_str function testing
    print("num_str() testing")
    print(" Case 1: Expected: {'1': 'one', '2': 'two', '3': 'three'}, Result-", num_str(1, 3))
    print(" Case 2: Expected: {'2': 'two', '3': 'three', '4': 'four', '5': 'five'}, Result-", num_str(2, 5))
    print(" Case 3: Expected: {'5': 'five', '6': 'six', '7': 'seven', '8': 'eight'}, Result-", num_str(5, 8))
    print(f"{'-' * 50}\n")

    
    # common_num function testing
    list_a = [1, 2, 3, 4]
    list_b = [3, 4, 5, 6]
    print("common_num() testing")
    print(f"Common numbers Expected: 1, 2, Result - {common_num(list_a, list_b)}")
    print(f"{'-' * 50}\n")


    # num_str function testing
    test_string = 'Find all of the words in a string that are less than 5 letters'
    print("Short Words function testing:")
    print("Expected: ['Find', 'all', 'of', 'the', 'in', 'a', 'that', 'are', 'less', 'than', '5'], Result -", short_words(test_string))




