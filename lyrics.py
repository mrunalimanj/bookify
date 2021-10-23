import lyricsgenius as lg


genius = lg.Genius('jGsEduMlXVJYax0PeN-qyaDyR3CkzmihrvJ105__UwAEBJSIBEmpn_lJ-W0Nt-n_', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)


# This functions return a string with all of the song lyrics for the song inputted.
def getSong(songName, artistName):
    try:
        song = genius.search_song(songName, artistName)
        lyrics = song.lyrics
        return lyrics
    except:
        print("Error when fetching song lyrics.")

# This function returns a list of song lyrics for the count number of songs that are most popular from the artist inputted.
def getTopSongsForArtist(artistName, count):
    try:
        songs = (genius.search_artist(artistName max_songs=count, sort='popularity')).songs
        s = [song.lyrics for song in songs]
        return s
    except:
        print("Error when fetching song lyrics.")


