file_name = 'artist.txt'

try:
    with open(file_name) as file_obj:
        lines = file_obj.readlines()

except FileNotFoundError:
    print(f'Cannot find file {file_name}')

print('All done')