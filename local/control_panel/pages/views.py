# Create your views here.
import os

from datetime import datetime
import os
from django.shortcuts import render

def home(request):
    context = {"ts": datetime.now()}
    return render(request, 'home.html',context)

def listing(request, temp):
    context = {'dir_content': os.listdir('/var/log' + '/' + str(temp))}
    context['dir'] = []
    context['fils'] = []
    for t in context['dir_content']:
        if os.path.isdir(os.path.join('/var/log' + '/' + str(temp), t)):
            context['dir'].append(t)
        else:
            context['fils'].append(t)
    return render(request, 'listing.html', context)  
