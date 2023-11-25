from django.urls import path
from .views import *


urlpatterns = [
    path("", home_page_view, name="home"),
    path("login/", login_page_view, name="login"),
    path("logout/", logout_page_view, name="logout"),
    path('main/products', main_products_page_view, name="main-products"),
    path("main/product/<slug:product_slug>/", main_product_slug_page_view, name="product-slug"),
    path("operator/products", operator_products_page_view, name="operator-products")
]
