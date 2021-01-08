from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(req):

    if req.method == "POST":

        temp = req.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return render(req, 'accounts/hello_world.html', context={'hello_world_output': new_hello_world})
    else:
        return render(req, 'accounts/hello_world.html', context={'text': 'get method!!'})
