import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import json

def create_playlist(user, tracks, name, description):
    f = open("keys.json")
    data = json.load(f)
    cid = data['cid']
    secret = data['secret']
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    #spoauth = SpotifyOAuth(cid, secret, "https://github.com/mrunalimanj/bookify")
    #print(spoauth.get_authorize_url())
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(user, scope)
    sp = spotipy.client.Spotify(auth=token, client_credentials_manager=client_credentials_manager)
    done_indicate = input("Type done once you have logged in: ")
    playlist_data = sp.user_playlist_create(user, name, description=description)
    playlist_id = playlist_data["id"]
    sp.playlist_add_items(playlist_id, tracks, position=None)
    