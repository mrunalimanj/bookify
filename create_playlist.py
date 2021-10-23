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
    spoauth = SpotifyOAuth(cid, secret, "https://github.com/mrunalimanj/bookify")
    print(spoauth.get_authorize_url())
    sp = spotipy.client.Spotify(oauth_manager=spoauth, client_credentials_manager=client_credentials_manager)
    done_indicate = input("Type done once you have logged in: ")
    sp.user_playlist_create(user, name, description=description)
    for track in tracks:
        continue