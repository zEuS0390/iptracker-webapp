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
        data = specificIP.completeLocation(ip_address)
        return render(request, template_name="ip_api/result.html", context={"data": data})