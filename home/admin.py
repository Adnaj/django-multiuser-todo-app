from django.contrib import admin
from .models import *
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display=('title','status','user','date')
admin.site.register(Todo,TodoAdmin)
