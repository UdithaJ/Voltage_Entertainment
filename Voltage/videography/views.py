from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from videography.models import video_add
from videography.models import video_add2

# Create your views here.


def addvideo(request):
    if request.method == 'POST':
        if request.POST.get('Name') and request.POST.get('Contact') and request.POST.get('ContactEmail') and request.POST.get('fee'):
         saverecord=video_add()
         saverecord.Name = request.POST.get('Name')
         saverecord.Contact = request.POST.get('Contact')
         saverecord.ContactEmail  = request.POST.get('ContactEmail')
         saverecord.fee = request.POST.get('fee')
         saverecord.description = request.POST.get('fee')
         saverecord.save()
        return render(request,'video_add.html')
    else:
         return render(request,'video_add.html')
     
     
def displaytocustomer(request):return render(request,'cus_vid_profile.html')


def displayall(request):
    videogrpher = video_add.objects.all()
    return render(request,"display_all_vid.html",{'videogrpher':videogrpher})