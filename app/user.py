import json

from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return f"<User {self.name}>"

    # Operations the user can perform while using the application.
    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))

    def set_watched(self, name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True
            else:
                print(f'{name} not found in your movies. Please try again.')

    def save_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.json(), f)

    def json(self):
        # Write User instances with Movie's nested
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        # Read User instances and their Movies -> convert to iterables.
        user = User(json_data['name'])
        movies = []
        for movie in json_data['movies']:
            movies.append(Movie.from_json(movie))
        user.movies = movies
        return user
