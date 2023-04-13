from django.urls import path
# import views from portfolio
from . import views

# This declaration helps to find url paths by their name, calling particulary urls from this app
app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    # For django, if u put in url path an angle bracket it will search in the path for the:
    # 1.type of the variable given to the path <int>
    # 2.and after the calling Django is creating a variable passed to the function from views, in our case detail function

    path('<int:blog_id>/', views.detail, name='detail'),

]