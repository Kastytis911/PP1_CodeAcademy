import requests
from bs4 import BeautifulSoup


def read_url(url):

    resp = requests.get(url, allow_redirects=True)
    soup = BeautifulSoup(resp.content, "html.parser")
    print(soup.text)
    #print(resp.text)
    #print(resp.status_code)