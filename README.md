# Movies
### A basic way for you to keep track of the movies you have watched, or plan to in the future!

An application that tracks the movies you have watched, or not. Using command line input, a user can do any of the following options:
- See their list of movies.
- Mark a movie as Watched.
- Add a movie to their list of movies.
- List thier watched movies.
- Delete a movie.
- Save updates.
- Save and Exit

This is done by opening or creating (depending if present) a simple text file. Then performing the specified opperation to the instances saved to the file.

### Example file output:
```json
{
  "name": "example_user", 
  "movies": [{
    "name": "The Matrix", 
    "genre": "Sci-Fi/Action", 
    "watched": true,
  }, 
  {
    "name": "The Interview", 
    "genre": "Comedy", 
    "watched": true,
  }]
}
```

<br/>

### Some take-aways from this project:

This was made when I was first starting to learn Python. As such it is pretty simple, but demonstrates 
- *object oriented programming*, 
- scripted file storage, 
- user input, etc...  

If you would like to give it a try, feel free to clone/branch this repo and run **app.py** on your command line (no 3rd party requirements are needed).
