from django.urls import path
from . views import *

urlpatterns = [
    path('', index,name='bloghome'),
    path('blog-detail/<slug>',blog_detail,name='blog_detail'),



]
