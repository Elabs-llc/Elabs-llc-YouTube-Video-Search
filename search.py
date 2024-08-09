
# YouTube Video Search Python Program
# Search for YouTube Videos Using Python
# I was wondering how I could use Python to search for videos on YouTube without having to do it myself.

# And it was pretty simple!

# That’s one of the things I love about Python, it allows you to create programs quickly and with just a few lines of code.

### Let's begin...

# 1. Import the following packages
# - urllib.request 
# urllib.request will be used to get the HTML for the search results page on YouTube and print its HTML.

# - re
# re if for regular expression. You can find more details about this module [here](https://docs.python.org/3/library/re.html?highlight=re#module-re)

# - webbrowser
# This module is used to open links in a default browser. And it will be useful in opening our generated 
# search link in our browser

# - random
# used to randomly generate youtube link 

import urllib.request
import re
import webbrowser
import random

#### Ask user to enter a keyword or search term
search_keyword= input("Enter a word to search: ")

print(f'Searching YouTube for the search term {search_keyword.lower()}...')

#### search for the search term on YouTube
# Result will be displayed in html and we will use the urllib.request to get this
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword.replace(" ", "_").lower())

##### Results will be list of video ids
# let's find all videos on youtube with the search word
try:
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    # attach one video id to youtube link to open video
    url = "https://www.youtube.com/watch?v=" + random.choice(video_ids)

    urll = "https://www.youtube.com/watch?v=" + video_ids[0]

    # - Now open generated video ink in web browser
    webbrowser.open(url=urll)
    print('opening in your browser...')
except:
    print('Network error. Try again later!')
    
