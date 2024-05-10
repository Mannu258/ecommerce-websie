from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from .verifier import *


# Create your views here.
def index(request):
    product = Product.objects.all().order_by('-pub_date')
    context = {
        'product':product

    }
    return render(request,'shop/index.html',context)

def ProductView(request,id):
    product = Product.objects.filter(id=id)
    return render(request,'shop/productView.html',{'product':product})

def about(request):
    return render(request,'shop/about.html')

@login_required
def contact(request):
    if request.method=='POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        messege = request.POST.get('message')

        # print(name,email,phone,messege)
        ContactUs.objects.get_or_create(name=name,email=email,phone=phone,messege=messege)
        messages.info(request,'Thank you for contacting us You will be get call or email soon')
        return redirect("/shop/")
    return render(request,'shop/contact.html')
@login_required
def tracker(request):
    a = Order.objects.filter(user = request.user)

    return render(request,'shop/tracker.html',{'a':a})

def search(request):
    
    return render(request,'shop/search.html')
@login_required
def checkout(request,id):
    product = Product.objects.filter(id=id)
    try:
        if request.method == 'POST':
            user = request.user
            pro = Product.objects.get(id=id)
            first_name = request.POST.get('firstName')
            last_name = request.POST.get('lastName')
            number = request.POST.get('number')
            email = request.POST.get('email')
            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            country = request.POST.get('country')
            city = request.POST.get('city')
            zip = request.POST.get('zip')
            payment = request.POST.get('paymentMethod')
            Order.objects.get_or_create(user = user,product=pro,first_name=first_name,last_name= last_name,
                                        number=number,email=email,address1=address1,address2=address2,
                                        country=country,city=city,zip=zip,payment=payment)
            messages.info(request,'your order is successfully ordered check you order in my order section')
            return redirect("/shop/")

    except:
        messages.warning(request,'Something went went wrong try again')
        return redirect("/shop/")

        

    return render(request,'shop/checkout.html',{'product':product})

def register(request):
    if request.method =='POST':
       
        global username,password,email,name,number,OTP
        OTP = otpgenerator()
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        email2 = request.POST.get('email')
        name = request.POST.get('name')
        number = request.POST.get('number')
        print(username,password)
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request,"Username Taken By another")
            return redirect('/register/')
        try:
            email = EmailMessage(
                    subject='OTP for Creating Myawesome Cart Account',
                    body=f"Your One Time Password is {OTP}",
                    to=[f'{email2}']
)   
            email.send()
            return redirect('/shop/dashbord')
        except Exception as e:
            print(e)
    return render(request,'registration/register.html')

def otpverify(request):
    if request.method == 'POST':
        otp = int(request.POST.get('OTP'))
        print(otp , " " , OTP)
        if otp == OTP:
            details = UserDetails.objects.get_or_create(
            name = name,
            number = number,
            email = email,
            Username = username,
        )        
            user = User.objects.get_or_create(
            username = username,
            password = make_password(str(password)),
        )
            messages.info(request,'Accounts Created SuccessFully Now You can login')
            return redirect('/shop/')
        else:
            messages.info(request,'Wrong Otp Try again')
            return redirect('/shop/dashbord')
        
    return render(request, 'registration/verify.html')

@login_required
def logout_user(request):
    try:
        if request.method =='GET':
            logout(request)
            messages.success(request,'Successfully Logout')
            return redirect('/shop/')
    except Exception as e:
        print(e)
        return messages.success(request,'There was some error to do logout please login again')
    