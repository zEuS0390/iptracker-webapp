from django.urls import path
from .views import Index

app_name = "ip_api"
urlpatterns = [
    path("", Index.as_view(), name="index")
]