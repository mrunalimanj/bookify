import requests
import json

from requests.api import get

def title_query_request(title_name):
    res = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={title_name}")
    if res.status_code == 200:
        return json.loads(res.content)


def get_description_from_request(data):
    if data["totalItems"] == 0:
        return "no match found"
    else:
        # take top hit
        top_hit = data['items'][0]["volumeInfo"]
        isbns = top_hit["industryIdentifiers"]
        return top_hits["description"]

# top function
def get_description_from_title(title_name):
    data = title_query_request(title_name)
    return get_description_from_request(data)