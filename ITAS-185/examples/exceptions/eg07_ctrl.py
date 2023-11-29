while True:
    try:
        x = input('Enter something: ')
        print(x)
    except KeyboardInterrupt:
        print('gg - all done')
        break