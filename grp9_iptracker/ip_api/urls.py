from django.urls import path
from .views import Index, Result

app_name = "ip_api"
urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("result", Result.as_view(), name="result")
]