import requests
import json

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

def get_similarArtists(userInput_artist):
    # capture similar artists and urls
    similar_artist_array = []
    top_tracks_urls = []

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

        # build out array -- urls
        top_tracks_urls.append(get_topTracks(response_name_display))

    print("similar_artist_array ::")
    print(similar_artist_array)
    print("\n==============================\n")
    print("top_tracks_urls ::")
    print(top_tracks_urls)

    return None

def get_topTracks(response_name_display):
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

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# display all information
#jprint(r3.json())

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

    get_similarArtists(user_artist)

if __name__ == "__main__":
    main()
