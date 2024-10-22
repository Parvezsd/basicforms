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

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO': LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        em=request.POST['em']
        ur=request.POST['ur']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,email=em,url=ur)
        return HttpResponse('Webpage is created')
    return render(request,'insert_webpage.html',d)

def insert_Accessrecord(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    if request.method=='POST':
        na=request.POST['na']
        d=request.POST['d']
        a=request.POST['au']
        WO=Webpage.objects.get(pk=na)
        AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)
        return HttpResponse('AccessRecord is created')
    return render(request,'insert_accessrecord.html',d)

def select_multiple(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        MTN=request.POST.getlist('tn')
        EQST=Webpage.objects.none()
        for topic in MTN:
            EQST=EQST|Webpage.objects.filter(topic_name=topic)
        d1={'EQST':EQST}
        return render(request,'display_Webpage.html',d1)
    return render(request,'select_multiple.html',d)

def select_multiple_access(request):
    WTO=Webpage.objects.all()
    d={'WTO':WTO}
    if request.method=='POST':
        MN=request.POST.getlist('na')
        AQST=AccessRecord.objects.none()
        for name in MN:
            AQST=AQST|AccessRecord.objects.filter(name=name)
        d2={'AQST':AQST}
        return render(request,'display_Access.html',d2)
    return render(request,'select_multiple_access.html',d)