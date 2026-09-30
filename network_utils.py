import urllib.request
import json

def fetch_json(url):
    with urllib.request.urlopen(url) as response:
        data = response.read()
        return json.loads(data)

def is_url_accessible(url):
    try:
        urllib.request.urlopen(url)
        return True
    except:
        return False
