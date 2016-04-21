import os
import datetime
import urllib2

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
            'last_updated': datetime.datetime.utcnow(),
            'title': soup.title.string
        }

        return JsonResponse(data)


class DeployStatus(View):

    def get(self, request, *args, **kwargs):

        file_path = 'live_system_products/deploy_status.txt'

        status_file = open(file_path, 'r')

        full_file_contents = status_file.read()

        t = os.path.getmtime(file_path)
        modified_date = datetime.datetime.fromtimestamp(t)

        data = {
            'status': 'Failed',
            'last_updated': modified_date,
            'file_contents': full_file_contents
        }

        status_file.close()

        return JsonResponse(data)


class DeployReceiver(View):

    def post(self, request, *args, **kwargs):

        deploy_status = request.POST['deploy_message']

        file_path = 'live_system_products/deploy_status.txt'
        status_file = open(file_path, 'w')

        status_file.write(deploy_status)

        status_file.close()

        data = {
            'Success': True
        }

        return JsonResponse(data)
