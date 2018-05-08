# Movie Trailer Website

<b>This python script is used to generate a website which shows a variable amount of popular movies.</b>
<br>The amount of movies is set to 12 by default. 
<br><br>
Every movie is retrieved by using the themoviedb.org API and includes the title, story, poster image, 
a trailer url (youtube.com) and a link to buy or view the whole movie if available (amazon.com).

## An Udacity Project
The project is part of my Udacity course and uses some provided ressources.
<br><br>
<b>The requirements are exceeded by at least the following features or changes:</b>
<br>
<ul>
  <li>Movies are retrieved by an API (themoviedb.org)</li>
  <li>Movies show an option to buy or view on demand (amazon.com)</li>
  <li>A new layout was created which is also fully responsive</li>
  <li>Bootstrap and jQuery are upgraded to the latest versions</li>
  <li>All external ressources are now served over HTTP<b>S</b></li>
</ul>

## Installation
### Requirements
<ul>
  <li>A Windows, Mac or Linux machine with Python 2 or higher</li>
  <li>The Python library <i>requests</i> (see http://www.python-requests.org/en/latest/ or simply run "pip install -r requirements.txt" or "pip install requests")</li>
  <li>An API key from themoviedb.org (create an account and go to https://www.themoviedb.org/settings/api)</li>
</ul>

### Instruction
<ol>
  <li>Open the media.py file in an editor and enter your private themoviedb.org API in line 11, then save the file</li>
  <li>In a terminal / console of your choice, run the entertainment_center.py file</li>
  <li>Your webbrowser should now automatically open and show the fresh_tomatoes.html file with its movies</li>
  <li><i>Optional: Edit the number of returned movies in the entertainment_center.py file to a maximum of 20 movies. For layout purposes only settings of 6, 12 or 18 are recommended.</i></li>
</ol
<br><br>
<i>
Note:
Due to the Udacity requirement of beeing usable with Python 2, some Python 3 standards are not included unfortunately.
</i>
