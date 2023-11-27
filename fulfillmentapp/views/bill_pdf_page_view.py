from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.urls import reverse
from sendfile import sendfile

from fulfillmentapp.models import Delivery


class BillPdfPageView(View):
    def get(self, request, pk):
        my_model_instance = Delivery.objects.get(pk=pk)
        pdf_path = my_model_instance.pdf_file.path
        return sendfile(request, pdf_path, attachment=True, attachment_filename=f'{my_model_instance.pk}_document.pdf')
