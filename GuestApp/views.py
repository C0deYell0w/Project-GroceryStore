from django.shortcuts import render,redirect
from AdminApp.models import Products
from GuestApp.models import *
from django.contrib import messages
# Create your views here.

def guestindex(request):
    return render(request,"guestindex.html")

def Homepage(request):
    data = Products.objects.all()
    return render(request,"Home.html",{'Data':data})

def allproducts(request):
    data = Products.objects.all()
    return render(request,"allproducts.html",{'Data':data})

def detailedview(request,prodid):
    prod = Products.objects.get(id=prodid)
    similar_products = Products.objects.filter(Cat_Name=prod.Cat_Name).exclude(id=prod.id)
    return render(request,"Detailedview.html",{'Prod':prod,'SP':similar_products})

def selectedcat(request):
    products = Products.objects.all()
    selected_collection = request.GET.get('category')
    if selected_collection:
        products = products.filter(Cat_Name=selected_collection)
    return render(request,"selectedcat.html",{'products': products,'SC':selected_collection})

def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request,"contactus.html")

def signin_up(request):
    return render(request,"signup_signin.html")

def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        profile_picture = request.FILES['profile_picture'] if 'profile_picture' in request.FILES else None
        Users.objects.create(
            Name=name,
            Mobile=mobile,
            Gender=gender,
            Mail=email,
            UserName=username,
            Password=password,
            Profile_Picture=profile_picture, )
        return render(request, "Signup_signin.html")
    else:
        return render(request, "signup_signin.html")

def Sign_in(request):
    if request.method == "POST":
        UN = request.POST.get('username')
        PSW = request.POST.get('password')
        if Users.objects.filter(UserName = UN, Password = PSW).exists():
            request.session['UserName'] = UN
            request.session['Password'] = PSW
            return redirect('GuestApp:Homepage')
        else:
            return redirect('GuestApp:signin_up')
    return redirect('GuestApp:signin_up')

def Userlogout(request):
    del request.session['UserName']
    del request.session['Password']
    return redirect('GuestApp:signin_up')

def AddToCart(request):
    if request.method == 'POST':
        if 'UserName' in request.session:
            usrnam = request.session['UserName']
            Pnam = request.POST.get('prodname')
            Pdesc = request.POST.get('proddesc')
            price = request.POST.get('price')
            Quan = request.POST.get('quantity')
            total = request.POST.get('total')
            item = Cart(UserName=usrnam, Prod_Name=Pnam, Prod_Desc=Pdesc, Price=price, Quantity=Quan, Total=total)
            item.save()
            messages.success(request, 'Item successfully added to the cart.')
            return redirect('Guest:ViewCart')
        else:
            messages.error(request, 'Please log in to add to the cart.')
            return redirect('Guest:signin_up')
    else:
        return render(request, "productview.html")


def ViewCart(request):
    if 'UserName' in request.session:
        usrnam = request.session['UserName']
        cart_items = Cart.objects.filter(UserName=usrnam)
        Sub_Total = 0
        for i in cart_items:
            Sub_Total = Sub_Total+i.Total
        product_details = []
        for cart_item in cart_items:
            product = Products.objects.filter(Prod_Name=cart_item.Prod_Name).first()
            if product:
                product_details.append({'item': cart_item,'product': product,})
        return render(request, "cart.html", {'product_details': product_details, 'Sub_T':Sub_Total})
    else:
        return redirect('Guest:signin_up')

def DelFromCart(request,itemid):
    item=Cart.objects.filter(id=itemid)
    item.delete()
    return redirect("Guest:ViewCart")
