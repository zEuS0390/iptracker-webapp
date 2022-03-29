import requests
from urllib.parse import urljoin

def getIPInfo(ip_address):
    base_url = "https://ipapi.co/"
    url = urljoin(base_url, "{}/json".format(ip_address))
    data = requests.get(url).json()
    return data