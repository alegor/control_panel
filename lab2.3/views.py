# Create your views here.



from datetime import datetime
import os
import time
from django.shortcuts import render

def home(request):
    context = {"ts": datetime.now()}
    return render(request, 'home.html',context)

def listing(request, temp):
    context = {'dir_content': os.listdir('/var/log' + '/' + str(temp))}
    context['myTable'] = []
    for t in context['dir_content']:
        myStr = []
	mySize = os.path.getsize(os.path.join('/var/log' + '/' + str(temp), t))
	myTemp = os.stat(os.path.join('/var/log' + '/' + str(temp), t))
	myTime = time.localtime(myTemp.st_mtime)
	myStr.append(t)
	myStr.append(mySize)
	myStr.append(str(myTime[2])+':'+str(myTime[1])+':'+ str(myTime[0]))
	context['myTable'].append(myStr)
    return render(request, 'listing.html', context)  
