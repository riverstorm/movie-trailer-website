import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 4 CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css">
    <!-- jQuery -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <!-- Bootstrap 4 JS -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,800" rel="stylesheet">
    <!-- Extra CSS -->
    <link rel="stylesheet" type="text/css" href="css/style.css" media="screen" />
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.view-trailer', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
<body style="background-color:#1D2127;">
<!-- Trailer Video Modal -->
<div class="modal" id="trailer">
  <div class="modal-dialog">
    <div class="modal-content">
      <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
        <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
      </a>
      <div class="scale-media" id="trailer-video-container">
      </div>
    </div>
  </div>
</div>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="#">Top 12 Most Wanted Movies</a>
    <div class="collapse navbar-collapse justify-content-end">
        <span class="navbar-text">
          <img src="images/tmdb_logo.png" height="34px">
        </span>
    </div>
</nav>

<div class="flex-container p-2">
      {movie_tiles}
</div>

<div class="text-center">
    <img class="mt-5 mb-5" src="images/tmdb_logo.png" height="50px">
</div>

</body>

</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-xs-12 col-sm-12 col-md-12 col-lg-6 p-0 movie-tile float-left">
    <div class="flex-container m-2" style="background-image:url({poster_image_url});background-position: center; background-size: cover;">
        <div class="flex-container p-4" style="color:white; width:100%; height:100%; display:inline-block; background-color:rgba(0,0,0,0.8);">
            <img src="{poster_image_url}" width="220" height="342" class="float-left mr-4">
            <h3 class="mt-3">{movie_title}</h3>
            <p class="mt-3 mb-4">{movie_story}</p>
            <a class="btn btn-outline-light view-trailer" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">View Trailer</a>
            <a href="{buy_movie_link}" target="_blank" class="ml-2 btn btn-outline-warning" style="color: #ffc107;">Buy now</a>
        </div>
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_story=movie.story,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            buy_movie_link=movie.buy_movie_link
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)