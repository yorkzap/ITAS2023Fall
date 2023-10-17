# print 1a, 1b, 1c, 1d, 1e, 2a, 2b and so on

num_list = [1, 2, 3, 4]
letter_list = ['a', 'b', 'c', 'd', 'e']

new_list = []
for num in num_list:
    if num % 2 == 0:
        for letter in letter_list:
            new_list.append(str(num) + letter)

best_list = [str(num) + letter for num in num_list if num % 2 == 0 for letter in letter_list]

# print(new_list)
print(best_list)

if new_list == best_list:
    print("both are equal")