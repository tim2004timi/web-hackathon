from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest

from fulfillmentapp.get_users import get_seller


@user_passes_test(test_func=get_seller, login_url="/login/")
def main_requests_page_view(request: HttpRequest):
    """View главной страницы продавца с отгрузками"""
    pass
