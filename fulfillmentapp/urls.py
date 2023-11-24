from django.urls import path
from .views import *


urlpatterns = [
    path("", home_page_view, name="home"),
    path("login/", login_page_view, name="login"),
    path("logout/", logout_page_view, name="logout"),
    path('main/products', main_products_page_view, name="main-products"),
    path("operator/", operator_page_view, name="operator")
]
