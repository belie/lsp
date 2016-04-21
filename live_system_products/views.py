import os

from HTMLParser import HTMLParser
import urllib2

from django.http import JsonResponse
from django.views.generic import View, TemplateView

from bs4 import BeautifulSoup

class LspResults(TemplateView):
    template_name = 'index.html'

class QAStatus(View):

    def get(self, request, *args, **kwargs):

        response = urllib2.urlopen('http://python.org/')
        html = response.read()

        soup = BeautifulSoup(html, 'html.parser')

        print soup.title

        data = {
            'status': 'Good',
            'title': soup.title.string
        }

        return JsonResponse(data)


class DeployStatus(View):

    def get(self, request, *args, **kwargs):

        print os.getcwd()

        status_file = open('live_system_products/test.txt', 'r')

        full_file_contents = status_file.read()

        data = {
            'status': 'Failed',
            'file_contents': full_file_contents
        }

        status_file.close()

        return JsonResponse(data)
