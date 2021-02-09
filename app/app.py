import json
import os

from user import User


def menu():
    """Main interaction with application"""
    name = input("Please enter your name: ").lower()
    filename = f"storage/{name}.txt"

    # Create or Read a user instance (from file)
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)

        user = User.from_json(json_data)
    else:
        user = User(name)

    select_options = (
        "\nSelect an option:\n'S' - See your list of movies.\n'W' - Mark a movie as Watched.\n'A' - Add a movie to "
        "your list of movies.\n'L' - List your watched movies.\n'D' - Delete a movie.\n'F' - Save "
        "updates.\n'Q' to save and quit: \n")

    user_input = input(select_options).lower()

    while True:
        if user_input == 's':
            print("\n")
            for movie in user.movies:
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))

        elif user_input == 'w':
            movie_name = input("\nEnter the movie title to set as watched: \n").lower()
            user.set_watched(movie_name)

        elif user_input == 'a':
            movie_name = input("\nEnter the movie title: \n").lower()
            movie_genre = input("Enter the movie genre: \n").lower()
            user.add_movie(movie_name, movie_genre)

        elif user_input == 'l':
            for movie in user.watched_movies():
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))

        elif user_input == 'd':
            movie_name = input("Enter the movie title to be deleted: \n").lower()
            user.delete_movie(movie_name)

        elif user_input == 'f':
            user.save_file(filename)

        elif user_input == 'q':
            user.save_file(filename)
            break

        user_input = input(select_options).lower()


if __name__ == '__main__':
    menu()
