from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # html = "<html><body>Hello World!</body></html>"
    # return HttpResponse(html)
    # print(request.path)
    return HttpResponse('Hello Everybody...')
