from django.views import View
from django.shortcuts import redirect, render

# Create your views here.

class Index(View):

    def get(self, request):
        return render(request, template_name="ip_api/main.html")

    def post(self, request):
        return redirect("/")

class Result(View):

    def get(self, request):
        return render(request, template_name="ip_api/result.html")

    def post(self, request):
        return redirect("/")