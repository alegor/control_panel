# Create your views here.
import os
from datetime import datetime
from django.shortcuts import render
def home(request):
    context = {"ts": datetime.now()}
    return render(request, 'home.html',context)

def listing(request):
    dirs =  os.listdir("/var/log")
        
    context = {"dir_content": dirs}
    return render(request, 'listing.html',context)
