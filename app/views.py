from django.shortcuts import render
from app.models import *

# Create your views here.
def insert_topic(request):

    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()

        QLTO=Topic.objects.all()
        d={'QLTO':QLTO}
        return render(request,'display_topic.html',d)

    return render(request,'insert_topic.html')

def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={"QLTO":QLTO}

    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']

        TO=Topic.objects.get(topic_name=tn)
        NWO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        NWO.save()

        QLWO=Webpage.objects.all()
        d1={"QLWO":QLWO}
        return render(request,'display_webpage.html',d1)
        

    return render(request,'insert_webpage.html',d)



def insert_AR(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    if request.method=='POST':
        na=request.POST['na']
        da=request.POST['da']
        au=request.POST['au']

        WO=Webpage.objects.get(name=na)
        NAO=AccessRecord.objects.get_or_create(name=WO,date=da,author=au)[0]
        NAO.save()
        QLAO=AccessRecord.objects.all()
        d1={'QLAO':QLAO}
        return render(request,'display_AR.html',d1)

    return render(request,'insert_AR.html',d)































