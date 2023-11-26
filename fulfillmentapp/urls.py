from django.urls import path
from .views import *


urlpatterns = [
    path(route="", view=home_page_view, name="home"),

    path(route="login/", view=login_page_view, name="login"),
    path(route="logout/", view=logout_page_view, name="logout"),

    path(route="main/", view=main_redirect_view, name="main-redirect"),
    path(route='main/products/', view=main_products_page_view, name="main-products"),
    path(route='main/products/<str:filter>/<str:sorting>/',
         view=main_products_clear_data_page_view,
         name="main-products-clear-data"),
    path(route='main/bills/', view=main_bills_page_view, name="main-bills"),
    path(route='main/requests', view=main_requests_page_view, name="main-requests"),
    path(route="main/product/<slug:product_slug>/", view=main_product_slug_page_view, name="product-slug"),

    path(route="operator/", view=operator_redirect_view, name="operator-redirect"),
    path(route="operator/products", view=operator_products_page_view, name="operator-products")
]
