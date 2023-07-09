from django.shortcuts import render,redirect
from django.http import HttpResponse
from urlshortener.models import Url
# Create your views here.
def createUrl(req):
    if req.method=="POST":
       full_url=req.POST.get('full_url')
       obj=Url.create(full_url)
       return render(req,'urlshortener/index.html',{
          'full_url':obj.full_url,
          'short_url':req.get_host()+'/'+obj.short_url
       })
    return render(req,'urlshortener/index.html')

def routeTOURL(req,key):
    try:
       obj=Url.objects.get(short_url=key)
       return redirect(obj.full_url)
    except:
       return redirect(createUrl)
    #return redirect()