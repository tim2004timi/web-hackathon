from django.urls import path
from .views import login_page_view


urlpatterns = [
    path("", login_page_view, name="login")
]
