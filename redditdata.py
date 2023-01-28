import requests

response = requests.get("https://api.pushshift.io/reddit/search/submission/?q=tesla&subreddit=wallstreetbets")
print(response.json())

def get_request(url):
    """Get http request"""
    response = requests.get(url)
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

make_request("https://api.pushshift.io/reddit/search/submission/?subreddit=wallstreetbets")

words = ['cat','hat','mat']
for w in words:
    print(w)
