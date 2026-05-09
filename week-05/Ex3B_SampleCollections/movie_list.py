fav_movies = ["Eternity and a Day", "Interstellar", "The Time of The Gypsies", "Pulp Fiction"]
len_movie = len(fav_movies) 
print(f"The list fav_movies includes my top {len_movie} movies of all time.")
print(fav_movies)
print(sorted(fav_movies))
fav_movies.sort()
print(fav_movies)
# The .sort() method permanently changes the order of the list, while the sorted() function does not change the original list and returns a new sorted list.
fav_movies.append("Once upon a time in Anatolia")
fav_movies.sort()
print(fav_movies)
