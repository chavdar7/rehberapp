from django.urls import path
from .views import home, kisilist, kisiekle

urlpatterns = [
    path("", home, name="home"),
    path("home", home, name="home"),
    path("kisilist", kisilist, name="kisilist"),
    path("kisiekle", kisiekle, name="kisiekle"),
]
