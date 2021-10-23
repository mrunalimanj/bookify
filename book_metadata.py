import requests
import json

from requests.api import get

def title_query_request(title_name):
    title_name = title_name.replace(' ', "%20")
    res = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={title_name}")
    if res.status_code == 200:
        return json.loads(res.content)


def get_slim_metadata(data):
    if data["totalItems"] == 0:
        return "no match found"
    else:
        # take top hit
        top_hit = data['items'][0]["volumeInfo"]
        isbns = top_hit["industryIdentifiers"]
        # get isbn 13
        isbn_13 = [isbn["identifier"] for isbn in isbns if isbn["type"] == "ISBN_13"]
        book_metadata = {}
        book_metadata["ISBN_13"] = isbn_13
        book_metadata["description"] = top_hit["description"]
        return book_metadata

# top function
def get_slim_metadata_from_title(title_name):
    data = title_query_request(title_name)
    return get_slim_metadata(data)


def get_description(metadata):
    return metadata["description"]

def get_isbn(metadata):
    return metadata["ISBN_13"]