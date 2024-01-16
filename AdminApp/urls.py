from django.urls import path
from AdminApp import views
app_name="AdminApp"

urlpatterns = [
    path('indexpage/', views.indexpage,name="indexpage"),

    path('addcatpage/', views.addcatpage,name="addcatpage"),
    path('displaycatpage/', views.displaycatpage,name="displaycatpage"),
    path('EditCatpage/<int:catid>', views.EditCatpage, name="EditCatpage"),
    path('Updatecat/<int:catid>', views.Updatecat, name="Updatecat"),
    path('DeleteCat/<int:catid>', views.DeleteCat, name="DeleteCat"),

    path('Addprodpage/', views.Addprodpage, name="Addprodpage"),
    path('Displayproduct/', views.Displayproduct, name="Displayproduct"),
    path('Editprodpage/<int:prodid>', views.Editprodpage, name="Editprodpage"),
    path('Updateprod/<int:prodid>', views.Updateprod, name="Updateprod"),
    path('Deleteprod/<int:prodid>', views.Deleteprod, name="Deleteprod"),

    path('Loginpage', views.Loginpage, name="Loginpage"),
    path('Adminlogin/', views.Adminlogin, name="Adminlogin"),
    path('Adminlogout/', views.Adminlogout, name="Adminlogout"),

]