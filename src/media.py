import requests
import json

"""
Includes the Movie class to build the movie objects used on the web page
API key from themoviedb.org is required
"""


# Private key for themoviedb.org api
TMDB_APIKEY = 'YOUR API KEY HERE'


class Movie:
    """
    Movie objects are used to show main information about selected movies
    including a trailer and an option
    to buy or view the movie on amazon
    :def popular_movie: returns a list of currently most popular movies on
    themoviedb.org in descending order.
    :def search_trailer: builds the youtube url of a movie trailer by using
    themoviedb.org
    """
    def __init__(self, title, story, poster_image_url, trailer_youtube_url,
                 buy_movie_link):
        self.title = title
        self.story = story
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.buy_movie_link = buy_movie_link

    @staticmethod
    def popular_movie(amount):
        """
        Returns a list of currently most popular movies on themoviedb.org in
        descending order.
        :param amount: the amount of movies to include into the list. 20 movies
        is the maximum
        :return: list of current most popular movies
        """
        # The maximum amount of movies is limited to 20
        if amount > 20:
            amount = 20

        # Execute GET request to themoviedb.org to receive list of most popular
        # movies
        payload = {'api_key': TMDB_APIKEY, 'sort_by': 'popularity.desc'}
        r = requests.get('https://api.themoviedb.org/3/discover/movie',
                         params=payload)
        popular_movies = json.loads(r.text)

        # Create movie objects using the retrieved list
        popular_movies_list = []
        count = 0
        while amount > count:
            movie_id = popular_movies['results'][count]['id']
            if movie_id != 269149:
                movie_title = \
                    popular_movies['results'][count]['original_title']\
                    .encode('utf-8')
                movie_story = \
                    popular_movies['results'][count]['overview']\
                    .encode('utf-8')
                movie_story = (movie_story[:260] + '...') \
                    if len(movie_story) > 260 else movie_story
                movie_poster = 'https://image.tmdb.org/t/p/w500/' + \
                               popular_movies['results'][count]['poster_path']
                movie_trailer = \
                    Movie.search_trailer(
                        popular_movies['results'][count]['id'])
                buy_movie_link = 'https://www.amazon.com/s/url=search-alias' \
                                 '%3Dinstant-video&field-keywords=' \
                                 + movie_title

                # Build object
                popular_movie = Movie(movie_title, movie_story, movie_poster,
                                      movie_trailer, buy_movie_link)
                # Append objects to a list
                popular_movies_list.append(popular_movie)

            count += 1
            if movie_id == 269149:
                amount += 1

        return popular_movies_list

    @staticmethod
    def search_trailer(tmdb_id):
        """
        Returns a youtube url of a movie trailer from themoviedb.org.
        :param tmdb_id: the internal movie id from themoviedb.org
        :return: complete youtube url of a movies trailer
        """
        # Execute GET request to themoviedb.org to receive a trailer
        # informations
        payload = {'api_key': TMDB_APIKEY}
        r = requests.get('https://api.themoviedb.org/3/movie/{}/videos'
                         .format(tmdb_id), params=payload)
        trailer_result = json.loads(r.text)

        # Select the youtube key and build an url
        youtube_id = trailer_result['results'][0]['key']
        youtube_url = 'https://www.youtube.com/watch?v=' + youtube_id

        return youtube_url
