import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json

def create_playlist(user, tracks, name, description):
    f = open("keys.json")
    data = json.load(f)
    cid = data['cid']
    secret = data['secret']
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    spoauth = SpotifyOAuth(cid, secret, 'http://localhost/')
    print(spoauth.get_authorize_url())
    raise Exception()
    sp.user_playlist_create(user, name, description=description)