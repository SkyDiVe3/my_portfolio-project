from django.contrib import admin
from .models import Blog

#Registering a model means u approve to show it in admin panel
admin.site.register(Blog)