from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import redirect, render
from .api import getIPInfo

# Create your views here.

class Index(View):

    def get(self, request):
        return render(request, template_name="ip_api/main.html")

    def post(self, request):
        ip_address = request.POST.get("ip_address")
        data = getIPInfo(ip_address)
        if len(data["languages"]) > 50:
            data["languages"] = data["languages"][:50] + "\n" + data["languages"][50:]
        if len(data["org"]) > 50:
            data["org"] = data["org"][:50] + "\n" + data["org"][50:]
        return render(request, template_name="ip_api/result.html", context={"data": data})