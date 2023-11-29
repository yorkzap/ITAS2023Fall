print('Checking Assertions')

def evaluate_age(age : int) -> None:
    if age % 2 == 0:
        print('Age is even')
    else:
        print('Age is odd')
        
while True:
    x = input('Enter your age: (q to quit)')
    if x.lower == "q":
        break
    try:
        x = int(x)
        assert x != 0, "Infants do not count"
        assert x < 120, 'No one is that old. Except for Allan.'
        assert x > 0, 'Age must be greater than 0'
        evaluate_age(x)
    
    except AssertionError:
        print('Age must be greater than 0')
    
    except ValueError:
        print('Enter an integer please')