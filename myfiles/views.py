import datetime

from django.shortcuts import render
from myfiles.models import *

# Create your views here.
def index(malumot):
    maxs = Oyinlar.objects.all()
    if malumot.method == "POST":
        email = malumot.POST.get('chmail')
        emails(gmail=email).save()
    return render(malumot,'index.html',{'maxs': maxs})

def services(malumot):
    return render(malumot,'services.html')

def single(malumot):
    if malumot.method =="POST":
        ismi = malumot.POST.get('nom')
        familiya = malumot.POST.get('famil')
        email = malumot.POST.get('mail')
        sayt= malumot.POST.get('sayt')
        mal = malumot.POST.get('tet')
        vaqt= datetime.datetime.now()
        Kommentaria(Ismi=ismi,fam=familiya,emaili=email,text=mal,time=vaqt).save()
    return render(malumot,'single.html')

def sing(malumot):
    kom = Kommentaria.objects.all()
    return render(malumot,'single.html')


def main(malumot):
    return render(malumot,'main.html')

def about(malumot):
    ish = ishchilar.objects.all()
    if malumot.method =="POST":
        email = malumot.POST.get('chmail')
        emails(gmail=email).save()
    return render(malumot,'about.html',{'ishch': ish})

def contact(malumot):
    if malumot.method =="POST":
        ismi = malumot.POST.get('Name')
        familiya = malumot.POST.get('Fam')
        email = malumot.POST.get('Gmail')
        mal = malumot.POST.get('Malum')
        vaqt = datetime.datetime.now()
        Murojatlar(ismis=ismi,fam=familiya,mail=email,text=mal,time=vaqt).save()
    return render(malumot,'contact.html')











