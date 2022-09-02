from django.contrib import admin
from myfiles.models import *

# Register your models here.

class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Type,AdminType)

class AdminOyin(admin.ModelAdmin):
    list_display = ['id','nomi','tur','silka','vaqt','malumot','rasm']
admin.site.register(Oyinlar,AdminOyin)

class AdminIsh(admin.ModelAdmin):
    list_display = ['id','ism','fam','yosh','foto']
admin.site.register(ishchilar,AdminIsh)

class AdminMuroj(admin.ModelAdmin):
    list_display = ['id','ismis','fam','mail','text','time']
admin.site.register(Murojatlar,AdminMuroj)

class AdminKomment(admin.ModelAdmin):
    list_display = ['id','Ismi','fam','emaili','text','time']
admin.site.register(Kommentaria,AdminKomment)

class AdminGmail(admin.ModelAdmin):
    list_display = ['id','gmail']
admin.site.register(emails,AdminGmail)