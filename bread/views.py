from re import S
from django.shortcuts import redirect, render
from .models import person
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from parcing import t1
from parcing import t2
from parcing import t3
from parcing import d1
from parcing import d2
from parcing import d3
from interactions.models import Snippet


@login_required(login_url='login')
def home(request):
    text1 = t1
    text2 = t2
    text3 = t3
    date1 = d1
    date2 = d2
    date3 = d3
    objects = Snippet.objects.all()

    return render(request, 'index.html',{'text1':text1,'text2':text2,'text3':text3,'date1':date1,'date2':date2,'date3':date3, 'objects':objects})



def page2(request):
    data = person.objects.all()
    return render(request, 'page2.html', {'person':data})
    

def page3(request):
    return render(request, 'page3.html')

def sotr_kompanii(request):
    return render(request, 'sotr_kompanii.html')

def sotr_uroven(request):
    return render(request, 'sotr_uroven.html')



