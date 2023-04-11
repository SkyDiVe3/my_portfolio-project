from django.shortcuts import render
from .models import Blog
# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.all();
    # If u want to order/limit the showing of the elements from model u can:
    # blogs = Blog.objects.order_by(-date)[:5];
    # to order by date, so the newest 5 elements will pop up on top


    return render(request, 'blog/all_blogs.html', {'blogs': blogs})
