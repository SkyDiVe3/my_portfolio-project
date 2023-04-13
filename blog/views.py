# The function get_object_or_404 is particullary a function that controls if a object from model is
# passed or if not it will display the 404 error(missing error)
from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.all();
    # If u want to order/limit the showing of the elements from model u can:
    # blogs = Blog.objects.order_by(-date)[:5];
    # to order by date, so the newest 5 elements will pop up on top


    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    # This variable gets the value of the blog id(witch is primary key in the model), if it doesnt exist it pass a err
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})