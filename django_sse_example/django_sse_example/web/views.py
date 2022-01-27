# Create your views here.

from django.shortcuts import render
from django.views.generic import View
from django.template import RequestContext
from django.utils.timezone import now

from django_sse.views import BaseSseView

import time


class Home1(View):
    def get(self, request):
        return render(request, 'home.html', {})


class Home2(View):
    def get(self, request):
        return render(request, 'home2.html', {},)


class MySseEvents(BaseSseView):
    def iterator(self):
        while True:
            self.sse.add_message("date", str(now()))
            time.sleep(1)
            yield
