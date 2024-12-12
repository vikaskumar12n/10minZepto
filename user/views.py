from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.db import connection

def index(request):
    data=category.objects.all().order_by('-id')[0:12]
    sliderdata=slider.objects.all().order_by('-id')[0:3]
    pdata=myproduct.objects.all().order_by('-id')[0:18]
    opdata=myproduct.objects.filter(total_discount__gt=50)
    offerdata=offpic.objects.all().order_by('-id')[0:3]

    # print(x)
    md={'cdata':data,"sdata":sliderdata,"pdata":pdata,'odata':opdata ,'offpic':offerdata}
    return render(request,'user/index.html',md)

def aboutus(request):
    return render(request,'user/aboutus.html')
########################################################
def contectus(request):
    if request.method=='POST':
        a1=request.POST.get('name')
        a2=request.POST.get('email')
        a3=request.POST.get('contact')
        a4=request.POST.get('message')
       # print(a1,a2,a3,a4)
        contact(Name=a1,Email=a2,Mobile=a3,Message=a4).save()
        return HttpResponse("<script> alert('thank you for contacting with us....'); location.href='/user/contactus/'</script>")
                            
    return render(request,'user/contectus.html')

############################################
def signin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        x=register.objects.filter(email=email,password=password).count()
            #print(x)
        if x==1:
            y=register.objects.filter(email=email,password=password)
            request.session['user']=email
            request.session['userpic']=str(y[0].profile)
            request.session['username']=str(y[0].name)
            user=request.session.get('user')
            cartitems = cart.objects.filter(user_id=user).count()
            request.session['cartitems'] = cartitems
            return HttpResponse("<script>alert('login successful...');location.href='/user/signin/'</script>")
        else:
            return HttpResponse("<script>alert('Your userId or Password in incorrect...');location.href='/user/signin/'</script>")
    return render(request,'user/signin.html')


####################################################
def signup(request):
    if request.method=='POST':
       name=request.POST.get('name')
       email=request.POST.get('email')
       mobile=request.POST.get('mobile')
       password=request.POST.get('password')
       address=request.POST.get('address')
       pic=request.FILES['fu']
       x=register.objects.all().filter(email=email).count()
       if x==1:
           return HttpResponse("<script>alert(' you are already registered..');location.href='/user/signup/'</script>")
       else:
           register(name=name,email=email,mobile=mobile,password=password,address=address,profile=pic ).save()
           return HttpResponse("<script>alert('you are registeres successfully..');location.href='/user/signup/'</script>")
    return render(request,'user/signup.html')
####################################################
def product(request):
    catid=request.GET.get('cid')
    subcatid=request.GET.get('sid')
    sdata=subcategory.objects.all().order_by('-id')
    if subcatid is not None:
        pdata=myproduct.objects.all().filter(subcategory_name=subcatid)
    elif catid is not None:
        pdata=myproduct.objects.all().filter(product_category=catid)
    else:
        pdata=myproduct.objects.all().order_by('-id')
    md={"subcate":sdata, "pdata":pdata,}
    return render(request,'user/product.html',md)
def signout(request):
    if request.session.get('user'):
        del request.session['user']
        del request.session['userpic']
        return HttpResponse(" <script>location.href='/user/index/'</script>")
    return render(request,'user/signout.html')

def myprofile(request):
    user=request.session.get('user')
    if request.method=='POST':
       name=request.POST.get('name')
       mobile=request.POST.get('mobile')
       password=request.POST.get('password')
       address=request.POST.get('address')
       pic=request.FILES['fu']
       register(name=name,email=user,mobile=mobile,profile=pic,address=address,password=password).save()
       return HttpResponse("<script>alert('your profile is updated succsessfully....');location.href='/user/myprofile/'</script>")
    rdata=""
    if user:
        rdata=register.objects.all().filter(email=user)
    md={"rdata":rdata}
    return render(request,'user/myprofile.html',md)
def mycart(request):
    user=request.session.get('user')
    if user:
        qt=int(request.GET.get('qt'))
        pname=request.GET.get('pname')
        ppic=request.GET.get('ppic')
        pw=request.GET.get('pw')
        price=int(request.GET.get('price'))
        total_price= qt * price
        #print(qt,pname,ppic,pw,price,total_price)
        if qt>0:
            cart(user_id=user,product_name=pname,product_quantity=qt,price=price,total_price=total_price,product_picture=ppic,pw=pw,added_date=datetime.now().date()).save()
            cartitems=cart.objects.filter(user_id=user).count()
            request.session['cartitems']=cartitems
            return HttpResponse("<script>alert('your item added in cart..');location.href='/user/product/'</script>")
        else:
            return HttpResponse("<script>alert('please increase your cart item');location.href='/user/index/'</script>")
    return render(request,'user/mycart.html')

def cartitems(request):
    user=request.session.get('user')
    cid=request.GET.get('cid')
    cartdata=""
    if user:
        cartdata=cart.objects.filter(user_id=user)
        if cid is not None:
            cart.objects.filter(id=cid).delete()
            cartitems = cart.objects.filter(user_id=user).count()
            request.session['cartitems']=cartitems
            return HttpResponse("<script>alert('your cart item is remove successfully..');location.href='/user/cartitems/'</script>")
    md={"cartdata":cartdata}

    return render(request,'user/cartitems.html',md)
def indexcart(request):
    user = request.session.get('user')
    if user:
        qt=int(request.GET.get('qt'))
        pname = request.GET.get('pname')
        ppic = request.GET.get('ppic')
        pw = request.GET.get('pw')
        price =int(request.GET.get('price'))
        total_price = qt*price
        # print(qt,pname,ppic,pw,price,total_price)
        if qt>0:
            cart(user_id=user, product_name=pname, product_quantity=qt, price=price, total_price=total_price,
                 product_picture=ppic, pw=pw, added_date=datetime.now().date()).save()
            cartitems=cart.objects.filter(user_id=user).count()
            request.session['cartitems'] = cartitems
            return HttpResponse("<script>alert('your item added in cart..');location.href='/user/index/'</script>")
        else:
            return HttpResponse("<script>alert('please increase your cart item');location.href='/user/index/'</script>")
    return render(request,'user/indexcart.html')

def myorders(request):
    msg=request.GET.get('msg')
    user=request.session.get('user')
    if msg is not None:
        cursor=connection.cursor()
        cursor.execute("insert into user_myorder(product_name,product_quantity,price,total_price,product_picture,pw,user_id,status,order_date) select product_name,product_quantity,price,total_price,product_picture,pw,'"+str(user)+"','pending','"+str(datetime.now().date())+"' from user_cart where user_id='"+str(user)+"'")
        cart.objects.filter(user_id=user).delete()
        cartitems=cart.objects.filter(user_id=user).count()
        request.session['cartitems'] = cartitems
        return HttpResponse("<script>alert('your order has placed successfully...');location.href='/user/orderlist/'</script>")
        x=cursor.fetchall()
        print(x)

    return render(request,'user/myorder.html')
def orderlist(request):
    oid=request.GET.get('oid')
    user=request.session.get('user')
    pdata=myorder.objects.filter(user_id=user,status="pending")
    adata=myorder.objects.filter(user_id=user,status="accepted")
    ddata=myorder.objects.filter(user_id=user,status="delivered")
    if oid is not None:
        myorder.objects.filter(id=oid)

        return HttpResponse("<script>alert('your order has been cenceled...');location.href='/user/orderlist/'</script>")
    mydict={"pdata":pdata,"adata":adata,"ddata":ddata,}
    return render(request,'user/orderlist.html',mydict)


def myinformation(request):
     return render(request,'user/myinformation.html')