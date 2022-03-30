from abc import ABC, abstractmethod
from urllib.parse import urljoin
from decouple import config
import requests

field = {
    "ip": "ip_address",
    "city": "city_name",
    "region": "region_name",
    "region_code": "region_code",
    "country": "country_name",
    "country_code": "country_code_2letter",
    "country_code_iso3": "country_code_3ltter",
    "counrty_capital": "country_capital",
    "country_tld":"country_tld",
    "continent_code":"continent_code",
    "in_eu": False,
    "postal": "postal_code",
    "latitude" :"latitude",
    "longitude" :"longitude",
    "timezone": "timezone", # format area/location
    "utc_offset":"UTC_time",
    "country_calling_code":"calling_code",
    "currency": "currency_code",
    "currency_name": "currency_name",
    "languages":"language",
    "country_area": "area_country", #in sq km
    "counrty_population": "number_population",
    "asn": "autonomous_system_number",
    "org" : "organization_name",
    "hostname": "host_name",
}

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
    base_url = "http://ip-api.com"
    url = urljoin(base_url, "json/{}".format(ip_address))
    data = requests.get(url).json()
    return data
