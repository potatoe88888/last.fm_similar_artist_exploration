import requests
import json
from bs4 import BeautifulSoup

API_KEY = ''
USER_AGENT = ''
ARTIST_LIMIT = 20
TOP_TRACKS_LIMIT = 5

def lastfm_getData(payload):
    # use a header for last.fm to not block the request [https://www.last.fm/api/intro]
    headers = {'user-agent': USER_AGENT}
    url = 'https://ws.audioscrobbler.com/2.0/'

    # build payload
    payload['api_key'] = API_KEY
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, indent=4)
    print(text)

def get_similarArtists(userInput_artist):
    # capture similar artists and urls
    similar_artist_array = []
    results_dict = {}

    # build out payload -- artist name
    request_sa = lastfm_getData({
        'method': 'artist.getSimilar',
        'limit': ARTIST_LIMIT,
        'autocorrect': 1,                           # allows for mis-spells, decently works too!
        'artist': userInput_artist
    })

    for index_sa in range(0, ARTIST_LIMIT):
        # capture artist name
        response_name_display = request_sa.json()['similarartists']['artist'][index_sa]['name']

        # build out array -- artist name
        similar_artist_array.append(response_name_display)

        # build out dictionary
        results_dict[response_name_display] = {'last.fm_urls': [], 'YouTube_urls': []}
        results_dict[response_name_display]['last.fm_urls'] = [get_topTracksLASTFM(response_name_display)]
        current_lastFM_urls = results_dict[response_name_display]['last.fm_urls']
        results_dict[response_name_display]['YouTube_urls'] = [get_topTracksYOUTUBE(current_lastFM_urls)]

    print("similar_artist_array ::")
    print(similar_artist_array)
    print("\n==============================\n")
    print("last.fm urls and YouTube urls to explore ::")
    jprint(results_dict)

    return results_dict

def get_topTracksYOUTUBE(current_lastFM_urls):
    top_tracks_array = []

    # needed to go two layers deep to reach each url
    for item in current_lastFM_urls:
        for lastFM_urls in item:
            request = requests.get(lastFM_urls)
            soup = BeautifulSoup(request.text, 'html.parser')

            for link in soup.find_all('a'):
                found_url = link.get('href')
                if "youtube.com/watch?v=" in str(found_url):
                    # not to copy duplicates
                    if str(found_url) not in top_tracks_array:
                        top_tracks_array.append(found_url)

    return top_tracks_array

def get_topTracksLASTFM(response_name_display):
    top_tracks_array = []

    for index in range(0, TOP_TRACKS_LIMIT):
        # build out payload -- urls
        request_tt = lastfm_getData({
            'method': 'artist.getTopTracks',
            'limit': TOP_TRACKS_LIMIT,
            'page': 1,
            'autocorrect': 1,                        # allows for mis-spells, decently works too!
            'artist': response_name_display
        })
        # capture TOP_TRACKS_LIMIT amount of urls
        response_url_display = request_tt.json()['toptracks']['track'][index]['url']

        # build out array
        top_tracks_array.append(response_url_display)

    return top_tracks_array

def check_connections():
    # check connection set up -- expect '200'
    r = lastfm_getData({
        'method': 'artist.getSimilar',
        'limit': ARTIST_LIMIT,
        'autocorrect': 1,  # allows for mis-spells, decently works too!
        'artist': 'Cher'
    })

    return r.status_code

def main():
    print("status :: " + str(check_connections()))

    user_artist = input('Please enter an artist // ')
    print("\n==============================\n")

    get_similarArtists(user_artist)

if __name__ == "__main__":
    main()
