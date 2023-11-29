def evaluate_age(age : int) -> None:
    if age < 0:
        raise ValueError('Age cannot be negative')
    if age % 2 == 0:
        print('Age is even')
    else:
        print('Age is odd')

try:
    num = int(input('Enter your age: '))
    evaluate_age(num)
except ValueError as msg:
    print(msg)