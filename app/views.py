from django.shortcuts import render

# Create your views here.
import datetime
def built_in_filter(request):
    dt=datetime.datetime.now()
    d={'data':'Today is Saturday','c':2,'dt':dt}
    return render(request,'built_in_filter.html',d)
