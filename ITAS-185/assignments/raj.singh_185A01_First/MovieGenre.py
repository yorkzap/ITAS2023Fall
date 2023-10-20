"""
Course: ITAS 185 - Introduction to Programming
Assignment 01: Movie Genre Program
Description: A program that allows users to manage a movie list where they can add, update,
             remove, search, and display movies along with their genres. The program utilizes
             a dictionary where the movie's name is the key and the genre is the value.
"""

#Functions
def main():
    
    while True:  # Start an infinite loop
        # Display the menu options
        print(menu_options)

        # Prompt the user to enter their choice.
        choice = input("Enter your choice (1-6): ")

        # Error handling for values that are not between the options 1-6.
        while not choice.isdigit() or int(choice) < 1 or int(choice) > 6:
            choice = input(f"\nChoice wrong. {BOLD} Enter a number from 1-6 please: {ENDC} \n {menu_options}")

        # Convert choice back to integer for further processing
        choice = int(choice)

        # Call the choice_handler function with the choice value as the argument.
        choice_handler(choice)

        


def get_movie_name():
    movie_name = input("Enter the name of the movie: ")
    return movie_name

# A function to take in choice value (1-6) and perform the corresponding action.
def choice_handler(choice):
    # If choice is 1, add a movie and its genre to the dictionary.
    if choice in [1, 2, 3, 4]:  # Only prompt for movie name for choices 1-4
        movie_name = get_movie_name()

    if choice == 1:
        add_movie(movie_name)
    elif choice == 2:
        update_movie(movie_name)
    elif choice == 3:
        delete_movie(movie_name)
    elif choice == 4:
        genre_movie(movie_name)
    elif choice == 5:
        display_movies(movies)
    elif choice == 6:
        log_off()

def case_insensitive_search(movie_name, movies):
    """
    Perform a case-insensitive search for the movie in the movies dictionary."""
    return next((key for key in movies if key.lower() == movie_name.lower()), None)


def add_movie(movie_name):
    genre = input("Enter the genre of the movie: ")
    movies.update({movie_name: genre})
    print(f"\n{BOLD}Movie added successfully!{ENDC}\n")
    display_movies(movies)

def update_movie(movie_name):
    # if movie name (key) exists in the dictionary (movies) then prompt for genre and update it
    movie_key = case_insensitive_search(movie_name, movies)
    if movie_key:
        genre = input("Enter the genre of the movie: ")
        movies[movie_key] = genre
        print(f"\n{BOLD}Movie updated successfully!{ENDC}\n")
        display_movies(movies)
    else:
        print(f"{movie_name} is not found in the movie dictionary.")

def delete_movie(movie_name):
    movie_key = case_insensitive_search(movie_name, movies)
    if movie_key:
        movies.pop(movie_key)
        print(f"\n{BOLD}Movie deleted successfully!{ENDC}\n")
        display_movies(movies)
    else:
        print(f"{movie_name} is not found in the movie dictionary.")

def genre_movie(movie_name):
    # Using a case-insensitive check to find the movie
    movie_key = case_insensitive_search(movie_name, movies)
    if movie_key:
        print(f"\n{BOLD}The genre of the movie is: {movies[movie_key]}{ENDC}\n")
    else:
        print(f"{movie_name} is not found in the movie dictionary.")


def display_movies(movies):
    print(f"\n{BOLD}Here is the current list of movies and their genres:{ENDC}\n")
# Determine the width for movie name column by finding the movie name with the longest length
    max_movie_name_length = max([len(movie) for movie in movies.keys()])
    for movie, genre in movies.items():
        print(f"{movie:<{max_movie_name_length + 2}} - {genre}")
    

def log_off():
    print(f"\n{BOLD}Thank you for using the program!{ENDC}\n")
    exit()

# ANSI escape codes for 
BOLD = "\033[1m"
ENDC = "\033[0m"

# Prompt the user with a menu with options to add, update, delete, search, display the list or exit the program.
print(BOLD + "Welcome to your movie list. You may:" + ENDC)
menu_options = """
\t 1. Add a movie and its genre
\t 2. Update the genre of a movie
\t 3. Delete a movie from the list
\t 4. Search for a movie's genre
\t 5. Display the list of all movies and their genres
\t 6. Exit the program
"""

movies = {
    "Wall-E": "Animated",
    "Life of Brian": "Comedy",
    "The Matrix": "Sci-Fi",
    "Titanic": "Drama",
    "Toy Story": "Animated"
}

# Call the choice_handler function with the choice value as the argument.
main()