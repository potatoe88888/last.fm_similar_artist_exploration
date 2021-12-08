# last.fm_similar_artist_exploration

## important note
This program will be working while in the terminal, it take a decent amount of time to process, will need to look into why, or maybe figure out how to lower the time of processing.

## set up -- create last.fm API account
1. Go to last.fm site and fill out information for generating an API key, [Create_API_account](https://www.last.fm/api/account/create). You don't really need to place a callback URL or an application homepage -- did not utilize features that required these things.
2. Next screen, assumed everything checked out okay by last.fm, the 'API key' and 'Shared secret' will be given.
3. Place your 'API key' within the ```prototype.py```, line begins with ``API_KEY= ''``, fill between the ' '. Place the 'Registered to' name as the ``USER_AGENT = ''``, fill between the ' '. 
4. Save, you are ready to explore!

## running
1. THIS IS STILL A WORK-IN-PROCESS-PROGRAM.
2. Navigate to your directory which will hold this repository through terminal of choice.
3. Depending on your python PATH variable set up, you could be using 'python' or 'python3', figure this out before proceeding the user could also house another variable other than these for python running more info? check out [Source 1](http://net-informations.com/python/intro/path.html) and [Source 2](https://geek-university.com/python/add-python-to-the-windows-path/). Run (prototype.py).
```  
$python prototype.py
```  
--or --
```  
$python3 prototype.py
```
4. You will be prompted to enter an Artist.
```
status :: 200
Please enter an artist //
```
5. The program will output:
    - status code of the connection, expect 200 returned
    - array of similar artists (current limit is 20 artists)
    - dictionary of last.fm and YouTube urls of top tracks per similar artist (current limit is 5 tracks)
    - *NOTE :: YouTube url counts are more than 5, need to investigate what it is scraping that is not only limited to a top track video*
  
## sources
  - https://www.dataquest.io/blog/last-fm-api-python/
  - https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-49.php
  - https://stackoverflow.com/questions/44720682/does-the-lastfm-api-provide-youtube-links
  - https://realpython.com/python-main-function/
  - https://docs.python.org/3/library/functions.html#input
  - https://beautiful-soup-4.readthedocs.io/en/latest/
  - https://towardsdatascience.com/an-introduction-to-web-scraping-with-python-a2601e8619e5
