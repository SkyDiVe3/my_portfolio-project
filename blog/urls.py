from django.urls import path
# import views from portfolio
from . import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
]