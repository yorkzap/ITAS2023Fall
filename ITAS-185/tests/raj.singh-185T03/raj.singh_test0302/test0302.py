import classes.Account as ac

if __name__ == "__main__":
    acc1 = ac.Account('Bob', 20)
    acc2 = ac.Account('Tim', 10)
    acc3 = ac.Account('Charlie')
    try:
        acc4 = ac.Account()  # should be an error
    except TypeError as msg:
        print(f'***ERROR*** {msg}')

    try:
        acc5 = ac.Account('', 10)  # should be an error
    except TypeError as msg:
        print(f'***ERROR*** {msg}')

    try:
        acc6 = ac.Account('Error', 'Amount')  # should be an error
    except TypeError as msg:
        print(f'***ERROR*** {msg}')

    try:
        acc7 = ac.Account('Error', -1)  # should be an error
    except TypeError as msg:
        print(f'***ERROR*** {msg}')

    acc1.add_transaction(10)
    acc1.add_transaction(34)
    acc1.add_transaction(-15)
    acc1.add_transaction(100)
    acc1.add_transaction(-30)
    acc1.add_transaction(26)

    acc2.add_transaction(100)
    acc2.add_transaction(-70)
    acc2.add_transaction(10)
    acc2.add_transaction(15)

    acc3.add_transaction(25)
    acc3.add_transaction(50)
    acc3.add_transaction(-10)

    try:
        acc3.add_transaction('horse')  # should be an error
    except ValueError as msg:
        print(f'***ERROR*** {msg}')

    print(acc1)
    print(f'{acc1.owner} has a balance of ${acc1.balance:.2f}')
    print(f'{acc1.owner} has done {len(acc1)} transactions')

