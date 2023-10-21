"""
Course: ITAS 185 - Introduction to Programming
Assignment 01: Movie Genre Program
Description: A program that allows users to manage a movie list where they can add, update,
             remove, search, and display movies along with their genres. The program utilizes
             a dictionary where the movie's name is the key and the genre is the value.
"""

def main():
    print("This program allows you to manage your list of movies and their genres.")
    
    while True:
        display_menu()
        choice = get_user_choice()
        handle_choice(choice)


def continue_or_exit():
    """Ask the user if they'd like to continue making changes or exit."""
    if not confirmation(f"{BOLD}Do you want to continue browsing the movie app?{ENDC}\n"):
        log_off()
        exit()


def display_menu():
    print(f"{BOLD}{BLUE}Welcome to your movie list. You may:{ENDC}")
    print(menu_options)


def format_list(genre):
    """Formats the list genres for display for better readability."""
    return ', '.join(genre) if isinstance(genre, list) else genre


def get_user_choice():
    choice = input(f"{YELLOW}{BOLD}Enter your choice (1-6): {ENDC}")
    while not is_valid_choice(choice):
        choice = input(f"\n{BOLD}{RED}Oops! Invalid choice.{ENDC} Enter a number from 1-6 please:\n{menu_options}")
    return int(choice)


def is_valid_choice(choice):
    return choice.isdigit() and 1 <= int(choice) <= 6


def handle_choice(choice):
    if choice in [1, 2, 3, 4]:
        movie_name = get_movie_name()
        handle_movie_related_choice(choice, movie_name)
    elif choice == 5:
        display_movies()
        continue_or_exit()
    elif choice == 6:
        log_off()


def handle_movie_related_choice(choice, movie_name):
    if choice == 1:
        add_movie(movie_name)
    elif choice == 2:
        update_movie_genre(movie_name)
    elif choice == 3:
        delete_movie(movie_name)
    elif choice == 4:
        genre_movie(movie_name)
    
    continue_or_exit()


def get_movie_name():
    return input(f"{YELLOW}{BOLD}Enter the name of the movie: {ENDC}")


def get_genre():
    genres = input(f"{YELLOW}{BOLD}Enter the genre(s) of the movie (separated by comma if multiple): {ENDC}").split(",")
    return [genre.strip() for genre in genres]


def get_or_search_movie(movie_name):
    """Search for a movie using case-insensitive and partial match."""
    movie_key = case_insensitive_search_and_handle(movie_name)
    
    if not movie_key:
        matched_movies = search_movie_by_partial_name(movie_name)
        if matched_movies:
            movie_key = matched_movies[0]
    
    return movie_key


def genre_movie(movie_name):
    movie_key = get_or_search_movie(movie_name)
    if movie_key:
        display_message(f"Gotcha! The genre for '{movie_key}' is: {format_list(movies[movie_key])}", color=GREEN)



def case_insensitive_search_and_handle(movie_name, display_not_found=True):
    movie_key = next((key for key in movies if key.lower() == movie_name.lower()), None)
    
    if movie_key and confirmation(f"{BOLD}Is '{movie_key}' the movie you were referring to?{ENDC}\n"):
        return movie_key
    elif display_not_found:
        display_movie_not_found(movie_name)
    return None


def search_movie_by_partial_name(partial_name):
    """Returns movies from the dictionary that match the provided substring."""
    matched_movies = [movie for movie in movies if movie.lower().startswith(partial_name.lower())]
    
    if not matched_movies:
        print(f"\t There's no movie called {partial_name} in our list.\n")
        return []
    
    print(f"\tHowever, we found movies that match your search '{partial_name}': {format_list(matched_movies)}")
    
    if len(matched_movies) == 1:
        if confirmation(f"\t{BOLD}Is '{matched_movies[0]}' the movie you were referring to?{ENDC}\n"):
            return [matched_movies[0]]

    print("Multiple movies found starting with the given name. Please select one:")
    for i, movie in enumerate(matched_movies, 1):
        print(f"{i}. {movie}")

    while True:
        selected_index = input("Enter the number of the correct movie: ")
        if selected_index.isdigit() and 1 <= int(selected_index) <= len(matched_movies):
            return [matched_movies[int(selected_index) - 1]]
        print("Invalid choice. Please select a valid number.")


def confirmation(prompt_message):
    response = input(f"{prompt_message}\n (yes/no): ").strip().lower()
    return response == "yes"


def add_movie(movie_name):
    movie_key = case_insensitive_search_and_handle(movie_name, display_not_found=False)
    if movie_key:
        display_message(f"This movie already exists. To update its genre, please select option 2 from the main menu.", YELLOW)
    else:
        genres = get_genre()
        movies[movie_name] = genres if len(genres) > 1 else genres[0]
        display_message("Movie added successfully!", GREEN)


def update_movie_genre(movie_name):
    movie_key = get_or_search_movie(movie_name)
    if movie_key:
        genres = get_genre()  # This can either be a list or a single string (if only one genre is entered)
        movies[movie_key] = genres
        display_message(f"Movie genre for {movie_key} updated to {format_list(genres)}!", GREEN)


def delete_movie(movie_name):
    movie_key = get_or_search_movie(movie_name)
    if movie_key:
        if confirmation(f"{BOLD}Are you sure you want to delete the movie {movie_key}?{ENDC}"):
            del movies[movie_key]
            display_message(f"Movie {movie_key} deleted successfully!", GREEN)
        else:
            display_message(f"Deletion of movie {movie_key} cancelled.")


def display_movie_not_found(movie_name):
    display_message(f"{movie_name} is not found in the movie dictionary.", color=RED)


def display_message(message, color=None):
    
    if color == RED:
        print(f"\n{BOLD}{RED}{message}{ENDC}\n")
    elif color == GREEN:
        print(f"\n{BOLD}{GREEN}{message}{ENDC}\n")
    elif color == BLUE:
        print(f"\n{BOLD}{BLUE}{message}{ENDC}\n")
    elif color == YELLOW:
        print(f"\n{BOLD}{YELLOW}{message}{ENDC}\n")
    else:
        print(message)


def pagination(movie_list, page, page_size=1000):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return movie_list[start_index:end_index]


def display_movies():
    PAGE_SIZE = 5  # Titles shown per page
    
    print(f"\n{BOLD}{BLUE}Here is the current list of movies and their genres:{ENDC}\n")
    max_movie_name_length = max([len(movie) for movie in movies.keys()])
    
    # Convert dictionary to list for easy indexing
    movie_list = list(movies.items())
    num_pages = len(movie_list) // PAGE_SIZE + (1 if len(movie_list) % PAGE_SIZE else 0)

    current_page = 1
    while current_page <= num_pages:
        for movie, genre in pagination(movie_list, current_page, PAGE_SIZE):
            print(f"{movie:<{max_movie_name_length + 2}} - {format_list(genre)}")

        # If there's another page, ask the user if they want to see it
        if current_page < num_pages:
            proceed = input(f"\n{BOLD}Displaying page {current_page}/{num_pages}. {BLUE}Would you like to see the next page?{ENDC} \n(yes/no) ").strip().lower()
            if proceed != 'yes':
                break
            current_page += 1
        else:
            break

    print("\n")


def log_off():
    display_message("Thank you for using the program!", GREEN)
    exit()


# ANSI escape codes
BOLD = "\033[1m"     # Makes the text bold
ENDC = "\033[0m"     # Resets all formatting to the default
GREEN = "\033[92m"   # Sets the text color to green
RED = "\033[91m"     # Sets the text color to red
BLUE = "\033[94m"    # Sets the text color to blue
YELLOW = "\033[93m"  # Sets the text color to yellow

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
    "Toy Story": "Animated",
    "Inception": "Sci-Fi",
    "The Godfather": "Drama",
    "Jurassic Park": "Adventure",
    "Shrek": "Animated",
    "Pulp Fiction": "Crime",
    "The Dark Knight": "Action",
    "Frozen": "Animated",
    "Jaws": "Thriller",
    "The Shawshank Redemption": "Drama",
    "Avatar": "Sci-Fi",
    "Finding Nemo": "Animated",
    "Forrest Gump": "Drama",
    "A Beautiful Mind": "Drama",
    "Braveheart": "Historical",
    "Despicable Me": "Animated",
    "Interstellar": "Sci-Fi",
    "The Hangover": "Comedy",
    "Iron Man": "Action",
    "Up": "Animated",
    "Mad Max: Fury Road": "Action"
}


if __name__ == '__main__':
    main()
