from django.urls import path
from . views import *

urlpatterns = [
    path('', index,name='Shophome'),
    path('product-view/<int:id>', ProductView,name='Details'),
    path('about/', about,name='AboutUs'),
    path('contact/', contact,name='ContactUs'),
    path('tracker', tracker,name='TrackingStatus'),
    path('search/', search,name='Search'),
    path('checkout/<int:id>', checkout,name='Checkout'),
    path('logout', logout_user ,name='logoutapp'),
    path('dashbord', otpverify ,name='dashbord'),






]
