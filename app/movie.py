class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return f"<Title: {self.name}>"

    def json(self):
        # Expected format for read/write Movie obj's.
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }

    @classmethod
    def from_json(cls, json_data):
        # Returns Movie instances associated with the user.
        return Movie(**json_data)
