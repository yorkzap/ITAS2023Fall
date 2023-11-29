
print('Enter two numbers. I will divide them')

while True:
    x = input('First number: (q to quit): ')
    if x.lower() == 'q':
        break
    y = input('Second number: (q to quit): ')
    if y.lower() == 'q':
        break
    try:
        result = int(x) / int(y)
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except ValueError:
        print('You must enter an integer')
    else:
        print(f'The result is {result}')
