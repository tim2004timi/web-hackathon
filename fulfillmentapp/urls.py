from django.urls import path
from .views import *


urlpatterns = [
    path("", home_page_view, name="home"),
    path("login/", login_page_view, name="login"),
    path('main/', main_page_view, name="main"),
    path("logout/", logout_page_view, name="logout")
]
