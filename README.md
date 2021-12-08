# last.fm_similar_artist_exploration

## set up -- create last.fm API account
1. Go to last.fm site and fill out information for generating an API key, [Create_API_account](https://www.last.fm/api/account/create). You don't really need to place a callback URL or an application homepage -- did not utilize features that required these things.
2. Next screen, assumed everything checked out okay by last.fm, the 'API key' and 'Shared secret' will be given.
3. Place your 'API key' within the ```prototype.py```, line begins with ``API_KEY= ''``, fill between the ' '. Place the 'Registered to' name as the ``USER_AGENT = ''``, fill between the ' '. 
4. Save, you are ready to explore!

## running
1. THIS IS STILL A WORK-IN-PROCESS-PROGRAM, made within 2 hours... no user interface... yet! Place your desired artist name within the last line of ```prototype.py```. For example, try "Apparat" as a replace of "Cold Play" within the code as shown below.
```
# example use case
get_similarArtists("Cold Play") 
```
2. Navigate to your directory which will hold this repository through terminal of choice.
3. Depending on your python PATH variable set up, you could be using 'python' or 'python3', figure this out before proceeding the user could also house another variable other than these for python running more info? check out [Source 1](http://net-informations.com/python/intro/path.html) and [Source 2](https://geek-university.com/python/add-python-to-the-windows-path/). Run (prototype.py).
```  
$python prototype.py
```  
--or --
```  
$python3 prototype.py
```
4. The program will output:
    - status code of the connection, expect 200 returned
    - array of similar artists (current limit is 20 artists)
    - array of urls for last.fm top tracks (current limit is 5 tracks)
  
## sources
  - https://www.dataquest.io/blog/last-fm-api-python/
  - https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-49.php
  - https://stackoverflow.com/questions/44720682/does-the-lastfm-api-provide-youtube-links
