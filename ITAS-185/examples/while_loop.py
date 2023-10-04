#Then use a while loop to display the square and cube of all the integers between 1 and a value input by the user (inclusive).

input_number = int(input("Enter the number that is less than 10 "))

if input_number < 10:
    i = 1
    while i <= input_number:
        square = i ** 2
        cube = i ** 3
        print(f"square: {square} cube: {cube}")
        i += 1
else:
    print("number is bigger than 10")


