from urllib.parse import urljoin
import requests

def getIPInfo(ip_address):
    base_url = "http://ip-api.com"
    url = urljoin(base_url, "json/{}".format(ip_address))
    data = requests.get(url).json()
    return data
