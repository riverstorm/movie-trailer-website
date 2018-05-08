import media
import fresh_tomatoes

"""
This file is used to request the generation of a website
The website is filled with a variable amount of popular movies
"""


# Get a list of a variable amount of popular movies
movies = media.Movie.popular_movie(8)

# Generate web page with the 12 popular movies
fresh_tomatoes.open_movies_page(movies)
