from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    html = "<html><body>Hello World!</body></html>"
    return HttpResponse(html)
