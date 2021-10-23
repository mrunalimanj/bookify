import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

def get_song_uris(query):
    f = open("keys.json")
    data = json.load(f)
    cid = data['cid']
    secret = data['secret']
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    uris = []
    track_results = sp.search(q=query, type='track', limit=15)
    for i, t in enumerate(track_results['tracks']['items']):
        uris.append(t['uri'])
    print(uris)
    return uris