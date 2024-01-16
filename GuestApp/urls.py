from django.urls import path
from GuestApp import views
app_name="GuestApp"

urlpatterns = [
    path('guestindex/', views.guestindex,name="guestindex"),
    path('Homepage/', views.Homepage,name="Homepage"),
    path('allproducts/', views.allproducts,name="allproducts"),
    path('detailedview/<int:prodid>/', views.detailedview,name="detailedview"),
    path('selectedcat/', views.selectedcat,name="selectedcat"),
    path('aboutus/', views.aboutus,name="aboutus"),
    path('contactus/', views.contactus,name="contactus"),

    path('signin_up/', views.signin_up,name="signin_up"),
    path('sign_up/', views.sign_up,name="sign_up"),
    path('Sign_in/', views.Sign_in,name="Sign_in"),
    path('Userlogout/', views.Userlogout,name="Userlogout"),

    path('ViewCart/', views.ViewCart,name="ViewCart"),



]