import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def create_playlist(user, tracks, name, description):
    cid = #ENTER CLIENT ID
    secret = #ENTER CLIENT SECRET
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.user_playlist_create(user, name, description=description)