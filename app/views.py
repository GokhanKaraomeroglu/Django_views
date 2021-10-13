from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # html = "<html><body>Hello World!</body></html>"
    # return HttpResponse(html)
    # print(request.path)
    # return HttpResponse('Hello Everybody...')
        context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
        return render (request, 'app/home.html', context)
