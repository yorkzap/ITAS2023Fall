"""
Course: ITAS 185 - Introduction to Programming
Test02: 02
Description:
    Reading list of words from text file and create further lists
    First with words starting from letter C and second with words that finish with letter H.
    Finally, writing the output to 'output.txt'. The first 10 start with C and the last 10 end in h
"""

def read_file_words(text_file):
    """Reading from text file and returning split lines"""
    with open(text_file, 'r') as file:
        return file.read().splitlines()

def write_file_words(text_file, words):
    """Writing single word per line"""
    with open(text_file, 'w') as file:
        for i in words:
            file.write(i + '\n')

def add_file_words(text_file, words):
    """Appending single word per line to the text file"""
    with open(text_file, 'a') as file:
        for i in words:
            file.write(i + '\n')

# Variable creation and path given
input_file = 'input.txt'
output_file = 'output.txt'

# Reading word list
all_words = read_file_words(input_file)

# Creating word list starting with C & ending with h
start_c = [word for word in all_words if word.startswith('C')]
end_c = [word for word in all_words if word.endswith('h')]

# Writing C words and h words to the output file
write_file_words(output_file, start_c)
add_file_words(output_file, end_c)


