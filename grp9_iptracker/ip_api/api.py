from abc import ABC, abstractmethod
from urllib.parse import urljoin
from decouple import config
import requests

class IPAPI(ABC):
    @abstractmethod
    def completeLocation(self): ...
    @abstractmethod
    def specificLocationFied(self): ...

class SpecificIP(IPAPI):

    def completeLocation(self, ip):
        """
        HTTP Request
        GET `https://ipapi.co/{ip}/json/`
        """
        url = urljoin(config("base_url"), f"/{ip}/json/")
        response = requests.get(url)
        return response.json(), response.status_code

    def specificLocationFied(self, ip, field):
        """
        HTTP Request
        GET `https://ipapi.co/{ip}/{field}/`
        """
        url = urljoin(config("base_url"), f"{ip}/{field}")
        response = requests.get(url)
        return response.text, response.status_code

class ClientIP(IPAPI):

    def completeLocation(self):
        """
        HTTP Request
        GET `https://ipapi.co/json/`
        """
        url = urljoin(config("base_url"), "json")
        response = requests.get(url)
        return response.json(), response.status_code

    def specificLocationFied(self, field):
        """
        HTTP Request
        GET `https://ipapi.co/{field}/`
        """
        url = urljoin(config("base_url"), f"{field}")
        response = requests.get(url)
        return response.text, response.status_code

def getIPInfo(ip_address):
    base_url = "http://ip-api.com"
    url = urljoin(base_url, "json/{}".format(ip_address))
    response = requests.get(url)
    return response.json(), response.status_code
