from django.shortcuts import render # type: ignore
from app.models import *
from django.http import HttpResponse # type: ignore
# Create your views here.
def basicforms(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)
        return HttpResponse(f'{tn} Topic is Created')
    return render(request,'basicforms.html')
def webpage(request):
    if request.method=='POST':
        tn=request.POST['tn']
        n=request.POST['na']
        u=request.POST['url']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=em)

        return HttpResponse('Topic is Created')
    return render(request,'webpage.html')

def accessrecord(request):
    if request.method=='POST':
        n=request.POST['na']
        d=request.POST['d']
        a=request.POST['au']
        WO=Webpage.objects.get(name=n)
        AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)
        return HttpResponse('AccessRecord is created')
    return render(request,'accessrecord.html')