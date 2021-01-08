from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(req):

    if req.method == "POST":
        return render(req, 'accounts/hello_world.html', context={'text': 'post method!!'})
    else:
        return render(req, 'accounts/hello_world.html', context={'text': 'get method!!'})
