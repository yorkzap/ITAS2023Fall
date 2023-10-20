"""
Course: ITAS 185 - Introduction to Programming
Assignment 01: Movie Genre Program
Description: A program that allows users to manage a movie list where they can add, update,
             remove, search, and display movies along with their genres. The program utilizes
             a dictionary where the movie's name is the key and the genre is the value.
"""


def main():
    while True:
        display_menu()
        choice = get_user_choice()
        handle_choice(choice)


def display_menu():
    print(f"{BOLD}Welcome to your movie list. You may:{ENDC}")
    print(menu_options)


def get_user_choice():
    choice = input("Enter your choice (1-6): ")
    while not is_valid_choice(choice):
        choice = input(f"\nChoice wrong. {BOLD}Enter a number from 1-6 please:{ENDC}\n{menu_options}")
    return int(choice)


def is_valid_choice(choice):
    return choice.isdigit() and 1 <= int(choice) <= 6


def handle_choice(choice):
    if choice in [1, 2, 3, 4]:
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


def get_movie_name():
    return input("Enter the name of the movie: ")


def add_movie(movie_name):
    genre = input("Enter the genre of the movie: ")
    movies[movie_name] = genre
    display_message("Movie added successfully!")
    display_movies(movies)


def update_movie(movie_name):
    if movie_exists(movie_name):
        genre = input("Enter the genre of the movie: ")
        movies[movie_name] = genre
        display_message("Movie updated successfully!")
        display_movies(movies)
    else:
        movie_not_found_message(movie_name)


def delete_movie(movie_name):
    if movie_exists(movie_name):
        del movies[movie_name]
        display_message("Movie deleted successfully!")
        display_movies(movies)
    else:
        movie_not_found_message(movie_name)


def genre_movie(movie_name):
    if movie_exists(movie_name):
        display_message(f"The genre of the movie is: {movies[movie_name]}")
    else:
        movie_not_found_message(movie_name)


def movie_exists(movie_name):
    return movie_name in movies


def movie_not_found_message(movie_name):
    print(f"{movie_name} is not found in the movie dictionary.")


def display_message(message):
    print(f"\n{BOLD}{message}{ENDC}\n")


def display_movies(movies):
    print(f"\n{BOLD}Here is the current list of movies and their genres:{ENDC}\n")
    max_movie_name_length = max([len(movie) for movie in movies.keys()])
    for movie, genre in movies.items():
        print(f"{movie:<{max_movie_name_length + 2}} - {genre}")


def log_off():
    display_message("Thank you for using the program!")
    exit()


# ANSI escape codes
BOLD = "\033[1m"
ENDC = "\033[0m"

# Menu options
menu_options = """
\t 1. Add a movie and its genre
\t 2. Update the genre of a movie
\t 3. Delete a movie from the list
\t 4. Search for a movie's genre
\t 5. Display the list of all movies and their genres
\t 6. Exit the program
"""

# Sample movies dictionary
movies = {
    "Wall-E": "Animated",
    "Life of Brian": "Comedy",
    "The Matrix": "Sci-Fi",
    "Titanic": "Drama",
    "Toy Story": "Animated"
}

if __name__ == '__main__':
    main()
