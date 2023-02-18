import requests
from bs4 import BeautifulSoup

url = 'https://www.15min.lt/naujienos/aktualu/lietuva'
def read_url(url):

    resp = requests.get(url, allow_redirects=True)
    soup = BeautifulSoup(resp.content, "html.parser")
    print(soup.text)
    #print(resp.text)
    #print(resp.status_code)

read_url(url)