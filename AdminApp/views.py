from django.shortcuts import render, redirect
from AdminApp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def indexpage(request):
    return render(request,"index.html")
def addcatpage(request):
    if request.method == "POST":
        Cnam = request.POST.get('catname')
        Desc = request.POST.get('catdesc')
        Img = request.FILES['catimg']
        Category.objects.create(Cat_Name=Cnam, Cat_Desc=Desc, Cat_Image=Img)
        return render(request,"addcategory.html")
    else:
        return render(request,"addcategory.html")

def displaycatpage(request):
    data = Category.objects.all()
    return render(request,"DisplayCategories.html",{'data': data})

def EditCatpage(request,catid):
    cat = Category.objects.get(id=catid)
    return render(request, "EditCategory.html", {'Cat':cat})

def Updatecat(request,catid):
    if request.method == "POST":
        CatNam=request.POST.get("catname")
        CatDesc=request.POST.get("catdesc")
        try:
            Img = request.FILES['catimg']
            fs = FileSystemStorage()
            file = fs.save(Img.name,Img)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=catid).Cat_Image
        Category.objects.filter(id=catid).update(Cat_Name=CatNam,Cat_Desc=CatDesc,Cat_Image=file)
        return redirect("AdminApp:displaycatpage")

def DeleteCat(request,catid):
    cat=Category.objects.filter(id=catid)
    cat.delete()
    return redirect("AdminApp:displaycatpage")



def Addprodpage(request):
    data = Category.objects.all()
    if request.method == "POST":
        Cnam = request.POST.get('catname')
        Pnam = request.POST.get('prodname')
        Pdesc = request.POST.get('proddesc')
        Price = request.POST.get('price')
        Img = request.FILES['prodimg']
        Products.objects.create(Cat_Name=Cnam,Prod_Name=Pnam, Prod_Desc=Pdesc, Price=Price, Prod_Image=Img)
        return render(request,"AddProduct.html", {'data': data})
    else:
        return render(request, "AddProduct.html", {'data': data})

def Displayproduct(request):
    data = Products.objects.all()
    return render(request,"DisplayProducts.html",{'data': data})

def Editprodpage(request,prodid):
    prod = Products.objects.get(id=prodid)
    cat = Category.objects.all()
    return render(request, "EditProduct.html", {'Prod': prod, 'Cat': cat})

def Updateprod(request,prodid):
    if request.method == "POST":
        CatNam=request.POST.get("catname")
        ProdNam=request.POST.get("prodname")
        ProdDesc=request.POST.get("proddesc")
        Price=request.POST.get("price")
        try:
            Img = request.FILES['prodimg']
            fs = FileSystemStorage()
            file = fs.save(Img.name,Img)
        except MultiValueDictKeyError:
            file = Products.objects.get(id=prodid).Prod_Image
        Products.objects.filter(id=prodid).update(Cat_Name=CatNam, Prod_Name=ProdNam, Prod_Desc=ProdDesc, Price=Price, Prod_Image=file)
        return redirect("AdminApp:Displayproduct")

def Deleteprod(request,prodid):
    Prod=Products.objects.filter(id=prodid)
    Prod.delete()
    return redirect("AdminApp:Displayproduct")

def Loginpage(request):
    return render(request, "Login.html")

def Adminlogin(request):
    if request.method == "POST":
        Un = request.POST.get('user_name')
        Pwd = request.POST.get('pass_word')
        if User.objects.filter(username__contains=Un).exists():
            user = authenticate(username=Un, password=Pwd)
            if user is not None:
                login(request, user)
                request.session['username']=Un
                request.session['password']=Pwd
                return redirect("AdminApp:indexpage")
            else:
                return redirect("AdminApp:Loginpage")
        else:
            return redirect("AdminApp:Loginpage")

def Adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect("AdminApp:Loginpage")
