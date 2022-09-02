from django.db import models

# Create your models here.

class Type(models.Model):
    nomi = models.CharField(max_length=20)
    def __str__(self):
        return self.nomi

class Oyinlar(models.Model):
    nomi= models.CharField(max_length=40)
    malumot= models.TextField()
    rasm = models.ImageField(upload_to='media')
    tur = models.ForeignKey(Type,on_delete=models.CASCADE,)
    silka = models.URLField()
    vaqt = models.DateTimeField(auto_now=True)

class ishchilar(models.Model):
    ism = models.CharField(max_length=30)
    fam = models.CharField(max_length=30)
    yosh = models.IntegerField()
    taym = models.DateTimeField(auto_now=True)
    foto = models.ImageField(upload_to='media')

class Murojatlar(models.Model):
    ismis = models.CharField(max_length=30)
    fam = models.CharField(max_length=30)
    mail = models.EmailField()
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)

class Kommentaria(models.Model):
    Ismi =models.CharField(max_length=30)
    fam =models.CharField(max_length=20)
    emaili =models.EmailField()
    text =models.TextField()
    time =models.DateTimeField(auto_now=True)


class emails(models.Model):
    gmail =models.EmailField()






