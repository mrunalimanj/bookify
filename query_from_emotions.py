import text2emotion as te
from collections import Counter

def get_query(text):
    high = get_emotions_from_text(text)
    query = ""
    for e in high:
        print(e[0])
        query += (e[0])
        query += " "
    query += "songs"
    return query

def get_emotions_from_text(text):
    emotions = te.get_emotion(text)
    k = Counter(emotions)
    high = k.most_common(1)
    return high
