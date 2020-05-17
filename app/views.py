from django.shortcuts import render,redirect
from .models import short

import random,string
home='http://127.0.0.1:8000/get/'
i='http://127.0.0.1:8000/info/'
# Create your views here.
def geturl(ur):
    chars = string.ascii_lowercase
    short_url = ''.join(random.choice(chars) for i in range(5))
    try:
        short.objects.get(surl=short_url)
        geturl(ur)
    except:
        u = short.objects.create(lurl=ur,surl=short_url,views='0')
        return short_url

def index(request):
    if request.method=='POST':
        import re
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if not(re.match(regex, request.POST['lurl']) is not None):
            url=''
            error=1
            message='Error in the Url'
        else:
            error=0
            ss=geturl(request.POST['lurl'])
            url=home+ss
            message='Success'
        data={
            'error':error,
            'url':url,
            'success':1,
            'message':message,
            'iurl':i+ss,
        }
        return render(request,'index.html',data)
    else:
        return render(request,'index.html')


def get(request,u):
    try:
        s=short.objects.get(surl=u)
        s.views=int(s.views)+1
        s.save()
        return redirect(s.lurl)
    except:
        return redirect(home)

def info(request,u):
    s=short.objects.get(surl=u)
    d={
        'stat':1,
        'views':s.views,
        'surl':home+s.surl,
        'lurl':s.lurl}
    return render(request,'index.html',d)