from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    blog = blogmodel.objects.all().order_by('-created_at')
    return render(request,'blog/index.html',{'blog':blog})


def blog_detail(request,slug):
    blog_obj = blogmodel.objects.filter(slug = slug)
    return render(request,'blog/blog_details.html',{'blog_obj':blog_obj})