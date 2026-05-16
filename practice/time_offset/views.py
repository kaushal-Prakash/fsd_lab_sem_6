from django.shortcuts import render
import datetime

# Create your views here.
def time(request,offset):
    offset = int(offset)
    curr = datetime.datetime.now()
    future = curr + datetime.timedelta(hours=offset)
    past = curr - datetime.timedelta(hours=offset)
    return render(request,"time.html",context={
        "offset":offset,
        "future":future,
        "past":past,
        "curr":curr
    })