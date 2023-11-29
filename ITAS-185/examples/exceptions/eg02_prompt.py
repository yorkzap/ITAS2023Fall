while True:
    number_tickets = input("How many tickets do you want? ")
    try:
        number_tickets = int(number_tickets)
    except ValueError as e:
        print(f'Error {e}. Please try again')
    else:
        print(f'You ordered {number_tickets}')
        break
        
print('All done')