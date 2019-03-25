from django.views import View
# Create your views here.
from django.shortcuts import render, HttpResponse

class Home(View):
    def get(self, request):
        return HttpResponse('<h1>Xin chao</h1>')