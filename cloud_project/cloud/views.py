from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render

from cloud.models import Name
from .forms  import YourName

def index(request):
    return render(request, "index.html")

def get_name(request):
    names = []
    for name in Name.objects.all():
        names.append(name.name)
        print(names)
    if request.method=="POST":
        form = YourName(request.POST)
        if form.is_valid():
            Name.objects.create(name=form.cleaned_data['your_name'])
            return HttpResponseRedirect('/index/')
        
    elif request.method=="DELETE":
        for name in Name.objects.all():
            name.dlete()
    else:
        form = YourName()

    return render(request, "index.html", {'form':form, "names":names})

def delete(request):
    for name in Name.objects.all():
        name.delete()
    return HttpResponseRedirect('/index/')