from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

def index(request):
    carousle = Carousel.objects.all()
    category = Category.objects.all()[:12]
    categories = request.GET.get('category')
    if categories:
        product = Product.objects.filter(category=categories,is_available=True)[:20]
    else:
        product = Product.objects.filter(is_available=True)[:20]    
    print(categories)
    context = {
        'carousle' : carousle,
        'category' : category,
        'product':product
    }
    return render(request,"home.html",context=context)

def products(request):
    category = Category.objects.all()
    categories = request.GET.get('category')
    if categories:
        product = Product.objects.filter(category=categories,is_available=True)
    else:
        product = Product.objects.filter(is_available=True)    
    context = {
        'product':product,
        'category':category
    }
    return render(request,"product.html",context=context)
    
def register(request):
    if request.method == "POST":
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        city = request.POST.get('city')
        address = request.POST.get('address')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        mobile = request.POST.get('phone')

        if User.objects.filter(email=email).exists():
            messages.error(request,"Already have an Account")
        elif User.objects.filter(username=username).exists():
            messages.error(request,"Username not available")
        else:
            if password1 == password2:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password1)
                user.save()
                register = Register(user=user,name=user.first_name,city=city,address=address,pincode=pincode,state=state,mobile=mobile)
                register.save()
                messages.success(request,"You are Successfully registered")
                return redirect("/login")
            else:
                messages.error(request,"Passwords are not matching")              
    return render(request,"register.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"Loggedin Successfully")
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentials")        
    return render(request,"login.html")

def see(request,product_id):
    product = Product.objects.filter(id=product_id,is_available=True)
    context = {
        'product' : product
    }
    return render(request,"see.html",context=context)


def logout(request):
    auth.logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect("/")

def search(request):
    query = request.GET.get('search')
    if query:
        product = Product.objects.filter(name__icontains = query)
    else:
        return HttpResponse("nope")
    context = {
        'products' : product
    }        
    print(query)
    return render(request,"search.html",context=context)


import razorpay
client = razorpay.Client(auth=("rzp_test_FVgxuzBdJ9c4So", "4riLfbUSnTNTzkNFzoIqA7GD"))

@login_required
def buy(request,product_id):
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('/login')    
    product = Product.objects.get(id=product_id)
    order_amount = product.price * 100
    order_currency = 'INR'
    order_receipt = 'order_rcptid_{product.id}_{user.id}'
    data = {
        'amount' : order_amount,
        'currency' : order_currency,
        'receipt' : order_receipt
    }
    order = client.order.create(data=data)
    payment = Payment(user=user,product=product,status='FAIL',orderid=order.get('id'))
    payment.save()
    print(order)
    context={
        'product':product,
        'order': order
    }

    return render(request,"buy.html",context=context) 

@csrf_exempt
def verifypayment(request):
    if request.method == "POST":
        print(request.POST)
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature = request.POST.get('razorpay_signature')
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }
        client.utility.verify_payment_signature(params_dict)
        payment = Payment.objects.get(orderid = razorpay_order_id)
        payment.status = "success"
        payment.paymentid = razorpay_payment_id
        payment.save()

        user_product = Userproduct(user = payment.user, name=payment.user.first_name,payment=payment,product=payment.product,orderid=payment.orderid,paymentid=payment.paymentid,totalprice=payment.product.price)
        user_product.save()
        return redirect ('/orders')            
        
def orders(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    userproduct = Userproduct.objects.filter(user=user)

    context = {
        'userproducts' : userproduct
    }        
    return render(request,"order.html",context=context)       
