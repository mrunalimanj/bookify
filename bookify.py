import text2emotion as te
from collections import Counter
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

'''
text = "Young and quirky Louisa Lou Clark (Emilia Clarke) moves from one job to the next to help her family make ends meet. Her cheerful attitude is put to the test when she becomes a caregiver for Will Traynor (Sam Claflin), a wealthy young banker left paralyzed from an accident two years earlier. Will's cynical outlook starts to change when Louisa shows him that life is worth living. As their bond deepens, their lives and hearts change in ways neither one could have imagined. But Will doesn't change his mind. On the night of Will's flight to Switzerland, Louisa visits him one last time. They agree that the past six months have been the best in their lives. He dies shortly after in the clinic, and it is revealed that he left Louisa a considerable inheritance, meant to continue her education and to fully experience life. The novel ends with Louisa at a cafÃ© in Paris, reading Will's last words to her in a letter, that tell her to 'live well'."
emotions = te.get_emotion(text)
k = Counter(emotions)
high = k.most_common(3)
print(high)

query = ""
for e in high:
    print(e[0])
    query += (e[0])
    query += " "
query += "songs"
print(query)
'''

query = "love songs"

cid = '6a74fc22c07b43d49db2b99808422dfe'
secret = '1083f36ed3cd40eeb5b054778096c090'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uris = []
track_results = sp.search(q=query, type='track', limit=15)
for i, t in enumerate(track_results['tracks']['items']):
    print(t['uri'])
    uris.append(t['uri'])

print(uris)