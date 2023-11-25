from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect


@login_required(login_url="/login/")
def operator_redirect_view(request: HttpRequest):
    """View для перехода с main по умолчанию"""

    return redirect("operator-products")
