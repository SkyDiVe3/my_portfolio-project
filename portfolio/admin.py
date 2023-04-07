from django.contrib import admin

# Register your models here.
from .models import Project

#Registering a model means u approve to show it in admin panel
admin.site.register(Project)