from django.views import View
from django.shortcuts import render
from .api import *

# Create your views here.

class Index(View):

    def get(self, request):
        return render(request, template_name="ip_api/main.html")

    def post(self, request):
        ip_address = request.POST.get("ip_address")
        specificIP = SpecificIP()
        response = specificIP.completeLocation(ip_address)
        if response[1] != 200:
            response = getIPInfo(ip_address)
        # data = {"City": "San Jose del Monte", "Province":"Bulacan", "Country": "Philippines"}
        return render(request, template_name="ip_api/result.html", context={"data": response[0], "status_code": response[1]})