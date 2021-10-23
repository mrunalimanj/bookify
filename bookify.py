import create_playlist as cp
import get_reviews as gr
import query_from_emotions as qe
import get_song_uris as su

# Get book title from user
title = input("Title of book you are reading: ")

# Get description of book from title
text = gr.get_description_from_title(title)

# get the top two emotions conveyed in the description and form a query
query = qe.get_query(text)

# Get the URIs for songs that correlate to the query generated
uris = su.get_song_uris(query)

# Create playlist out of song URIs
cp.create_playlist('313hgvmzvhgvdlufnhxwairtxxna', uris, title, "blah")