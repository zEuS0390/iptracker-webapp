from urllib.parse import urljoin
from abc import ABC, abstractmethod
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
        url = urljoin(config("base_url"), f"{ip}/json/")
        return requests.get(url).json()

    def specificLocationFied(self, ip, field):
        """
        HTTP Request
        GET `https://ipapi.co/{ip}/{field}/`
        """
        url = urljoin(config("base_url"), f"{ip}/{field}")
        data = requests.get(url).text
        return data

class ClientIP(IPAPI):

    def completeLocation(self):
        """
        HTTP Request
        GET `https://ipapi.co/json/`
        """
        url = urljoin(config("base_url"), "json")
        data = requests.get(url).json()
        return data

    def specificLocationFied(self, field):
        """
        HTTP Request
        GET `https://ipapi.co/{field}/`
        """
        url = urljoin(config("base_url"), f"{field}")
        data = requests.get(url).text
        return data

def getIPInfo(ip_address):
    base_url = "https://ipapi.co/"
    url = urljoin(base_url, "{}/json".format(ip_address))
    data = requests.get(url).json()
    return data
