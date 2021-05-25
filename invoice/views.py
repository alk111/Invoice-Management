from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login
from datetime import date

def NAV(request):
    return render(request,'navigation.html')

def INDEX(request):
    return render(request,'index.html')

def USERLOGIN(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user:
                login(request,user)
                error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'login.html',d)

def USERNAV(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id = request.user.id)
    data = Signup.objects.get(user = user)
    d = {'user':user,'data':data}
    return render(request,'user_nav.html',d)

def ADMINLOGIN(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'admin-login.html',d)   
    
def ADMIN_NAV(request):
    if not request.user.is_staff:
        return redirect('ADMINLOGIN')
    return render(request,'admin_nav.html')

def VIEWUSERS(request):
    if not request.user.is_authenticated:
        return redirect('admin-login')
    user = Signup.objects.all()
    
    d = {'user':user}
    return render(request,'view_users.html',d) 

def DELETEUSERS(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin-login')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('view_users') 

def ADMINLOGOUT(request):
    logout(request)
    return redirect('admin-login')

def USERLOGOUT(request):
    logout(request)
    return redirect('login')

def USERPROFILE(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id = request.user.id)
    data = Signup.objects.get(user = user)
    d = {'user':user,'data':data}
    return render(request,'profile.html',d)

def EDITPROFILE(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id = request.user.id)
    data = Signup.objects.get(user = user)
    
    error = "true"
    if request.method == "POST":
        f = request.POST['firstname']
        l = request.POST['lastname']
        c = request.POST['contact']
        comp = request.POST['company']  
        p = request.POST['currency']
        e = request.POST['eid'] 
        user.first_name = f
        user.last_name = l
        data.contact = c
        user.company = comp
        user.currency = p
        user.username = e

        user.save()
        data.save()
        error="false"

    d = {'user':user,'data':data,'error':error}
    return render(request,'edit_profile.html',d)

def CHANGEPASSWORD(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    if request.method == 'POST':
        o = request.POST['pwd']
        n = request.POST['new_pwd']
        c = request.POST['cnfrm_pwd']
        if n == c:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "no"
        else:
            error = "yes"
    d = {'error':error}
    return render(request,'change_pwd.html',d)

def AddPlan(request):
    if not request.user.is_authenticated:
       return redirect('login')
    error = ""
    if request.method == "POST":
        b1 = request.POST['plan']
        s1 = request.POST['billing_period']
        n1 = request.POST['price']
        f1 = request.POST['pricing_model']  
        u1 = User.objects.filter(username = request.user.username).first()
        try:
            Plan.objects.create(user=u1,uploadingdate=date.today(),plan=b1,billing_period=s1,price=n1,pricing_model=f1)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'add_plan.html',d)

def AddSubscription(request):
    if not request.user.is_authenticated:
       return redirect('login')
    error = ""
    if request.method == "POST":
        b1 = request.POST['plan']
        s1 = request.POST['billing_cycle']
        n1 = request.POST['auto_collection']
        u1 = User.objects.filter(username = request.user.username).first()
        try:
            Subscription.objects.create(user=u1,uploadingdate=date.today(),plan=b1,billing_cycle=s1,auto_collection=n1)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'add_Subscription.html',d)    

def INVOICE(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id = request.user.id)
    plan = Plan.objects.filter(user = user)

    d = {'plan':plan}
    return render(request,'invoice.html',d) 

def view_invoice(request, id=None):
    user = User.objects.get(id = request.user.id)
    plan = Plan.objects.filter(user = user)

    context = {
        "company": {
            "name": "RFM 360",
            "address" :"xyz, zxy, ab 1345, IN",
            "phone": " XXX XXXX",
            "email": "contact@RFM 360.com",
        },
        "plan": plan,

    }
    return render(request, 'pdf_template.html', context)

def SIGNUP(request):
    error = ""
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        comp = request.POST['company']  
        p = request.POST['currency']
        e = request.POST['emailid'] 
        ps = request.POST['pwd']
        try:
            user = User.objects.create_user(username=e,password=ps,first_name=f,last_name=l)
            Signup.objects.create(user=user,contact=c)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'signup.html',d)   
