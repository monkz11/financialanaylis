import requests
import time
import json

def get_request(url):
    """Get http request"""
    response = requests.get(url)
    #Check whether pull is succesful
    assert response.status_code == 200
    return response.json()


def make_request(url, max_tries=5):
    """This function is to add in logic to request for more post submissions"""
    tries = 1
    while tries < max_tries:
        try:
            time.sleep(0.5)
            json_response = get_request(url)
            return json_response
        except:
            tries += 1
            print("Error.... trying to get request attempt {}".format(tries))
    return get_request(url)

d = make_request("https://api.pushshift.io/reddit/search/comment/?q=amc&subreddit=wallstreetbets&ssize=1")

pretty_json = json.dumps(d, indent=2)

print(pretty_json)