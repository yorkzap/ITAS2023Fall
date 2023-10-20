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

# Prompt the user if they want to continue
def continue_or_exit():
    """Ask the user if they'd like to continue making changes or exit."""
    if not confirmation(f"{BOLD}Do you want to continue browsing the movie app?{ENDC}\n"):
        log_off()
        exit()


def display_menu():
    print(f"{BOLD}Welcome to your movie list. You may:{ENDC}")
    print(menu_options)


def get_user_choice():
    choice = input(f"{BOLD}Enter your choice (1-6): {ENDC}")
    while not is_valid_choice(choice):
        choice = input(f"\nChoice wrong. {BOLD}Enter a number from 1-6 please:{ENDC}\n{menu_options}")
    return int(choice)


def is_valid_choice(choice):
    return choice.isdigit() and 1 <= int(choice) <= 6


def get_or_search_movie(movie_name):
    """Search for a movie. If not found by exact name, tries partial matching."""
    movie_key = case_insensitive_search_and_handle(movie_name, movies, display_not_found=False)
    if not movie_key:
        matched_movies = search_movie_by_partial_name(movie_name)
        
        if not matched_movies:
            display_movie_not_found(movie_name)
            continue_or_exit()
            return None

        if len(matched_movies) == 1:
            movie_key = matched_movies[0]
        else:
            movie_key = select_from_matched_movies(matched_movies)
    
    return movie_key


def select_from_matched_movies(matched_movies):
    """Given multiple matched movies, lets the user select one."""
    print("Multiple movies found starting with the given name. Please select one:")
    for i, movie in enumerate(matched_movies, 1):
        print(f"{i}. {movie}")
    selected_index = int(input("Enter the number of the correct movie: ")) - 1
    return matched_movies[selected_index]


def handle_movie_related_choice(choice, movie_name):
    if choice == 1:
        add_movie(movie_name)
    elif choice == 2:
        update_movie_genre(movie_name)
    elif choice == 3:
        delete_movie(movie_name)
    elif choice == 4:
        genre_movie(movie_name)

def handle_choice(choice):
    if choice in [1, 2, 3, 4]:
        movie_name = get_movie_name()
        handle_movie_related_choice(choice, movie_name)
    elif choice == 5:
        display_movies(movies)
    elif choice == 6:
        log_off()


def get_movie_name():
    return input(f"{BOLD}Enter the name of the movie: {ENDC}")


def get_genre():
    """Prompt the user to input genres for a movie."""
    genres = input(f"{BOLD}Enter the genre(s) of the movie (separated by comma if multiple): {ENDC}").split(",")
    return [genre.strip() for genre in genres]


def genre_movie(movie_name):
    movie_key = case_insensitive_search_and_handle(movie_name, movies, display_not_found=False)  # Notice the new argument here
    if not movie_key:
        # If movie is not found by exact name, try partial matching
        matched_movies = search_movie_by_partial_name(movie_name)
        
        if not matched_movies:
            display_movie_not_found(movie_name)
            continue_or_exit()
            return

        if len(matched_movies) == 1:
            movie_key = matched_movies[0]
        else:
            # If there are multiple matches, ask the user to select one
            print("Multiple movies found starting with the given name. Please select one:")
            for i, movie in enumerate(matched_movies, 1):
                print(f"{i}. {movie}")
            selected_index = int(input("Enter the number of the correct movie: ")) - 1
            movie_key = matched_movies[selected_index]

    display_message(f"Gotcha, the genre for {matched_movies[0]} movie is: {movies[movie_key]}")
    continue_or_exit()


def search_movie_by_partial_name(partial_name):
    """Returns movies from the dictionary that start with the provided substring."""
    matched_movies = [movie for movie in movies if movie.lower().startswith(partial_name.lower())]
    
    if not matched_movies:
        print(f"\t There's no movie called {partial_name} in our list.\n")
        return []

    print(f"\t We found matched movies for '{partial_name}': {matched_movies}")
    
    if len(matched_movies) == 1 and confirmation(f"{BOLD}Is '{matched_movies[0]}' the movie you were referring to?{ENDC}"):
        return [matched_movies[0]]

    print("Multiple movies found starting with the given name. Please select one:")
    for i, movie in enumerate(matched_movies, 1):
        print(f"{i}. {movie}")
    selected_index = int(input("Enter the number of the correct movie3: ")) - 1
    return [matched_movies[selected_index]]



def case_insensitive_search_and_handle(movie_name, movies, display_not_found=True):
    movie_key = next((key for key in movies if key.lower() == movie_name.lower()), None)
    
    if movie_key:
        if confirmation(f"{BOLD}Is '{movie_key}' the movie you were referring to?{ENDC}"):
            return movie_key
        else:
            if display_not_found:
                display_movie_not_found(movie_name)
            return None

    if not movie_key and display_not_found:
        display_movie_not_found(movie_name)
        return None
    
    return movie_key


def confirmation(prompt_message):
    """
    Prompts the user for a confirmation based on the provided message.
    Returns True if the user confirms, otherwise returns False.
    """
    response = input(f"{prompt_message} (yes/no): ").strip().lower()
    return response == "yes"


def display_current_movie_list():
    """Display the current list of movies."""
    display_message("Here is the current list of movies and their genres:")
    max_movie_name_length = max([len(movie) for movie in movies.keys()])
    for movie, genre in movies.items():
        print(f"\t{movie:<{max_movie_name_length + 2}} - {genre}")
    print()


def add_movie(movie_name):
    if movie_exists(movie_name):
        display_message(f"The movie {movie_name} already exists in the dictionary.")
    else:
        genres = get_genre()
        # If there's only one genre, save it as a string. If there's more than one, save them as a list.
        movies[movie_name] = genres if len(genres) > 1 else genres[0]
        display_message("Movie added successfully!")
        continue_or_exit()


def update_movie_genre(movie_name):
    movie_key = case_insensitive_search_and_handle(movie_name, movies, display_not_found=False)  # Notice the new argument here
    if not movie_key:
        # If movie is not found by exact name, try partial matching
        matched_movies = search_movie_by_partial_name(movie_name)
        
        if not matched_movies:
            display_movie_not_found(movie_name)
            continue_or_exit()
            return

        if len(matched_movies) == 1:
            movie_key = matched_movies[0]
        else:
            # If there are multiple matches, ask the user to select one
            print("Multiple movies found starting with the given name. Please select one:")
            for i, movie in enumerate(matched_movies, 1):
                print(f"{i}. {movie}")
            selected_index = int(input("Enter the number of the correct movie: ")) - 1
            movie_key = matched_movies[selected_index]
    
    genres = get_genre()
    # If there's only one genre, save it as a string. If there's more than one, save them as a list.
    movies[movie_key] = genres if len(genres) > 1 else genres[0]
    display_message("Movie genre updated successfully!")
    continue_or_exit()




def delete_movie(movie_name):
    movie_key = case_insensitive_search_and_handle(movie_name, movies)
    if not movie_key:
        return
    
    if confirmation(f"{BOLD}Are you sure you want to delete the movie {movie_key}?{ENDC} \n"):
        del movies[movie_key]
        print(f"\nMovie {movie_key} deleted successfully!\n")
    else:
        print(f"\nDeletion of movie {movie_key} cancelled.\n")
    
    continue_or_exit()


def movie_exists(movie_name):
    return movie_name in movies


def display_movie_not_found(movie_name):
    """Notify the user that a movie was not found in the dictionary."""
    display_message(f"{movie_name} is not found in the movie dictionary.")


def display_message(message):
    print(f"\n{BOLD}{message}{ENDC}\n")


def display_movies(movies):
    print(f"\n{BOLD}Here is the current list of movies and their genres:{ENDC}\n")
    max_movie_name_length = max([len(movie) for movie in movies.keys()])
    for movie, genre in movies.items():
        print(f"{movie:<{max_movie_name_length + 2}} - {genre}")
    print("\n")
    continue_or_exit()


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
