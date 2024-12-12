from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('aboutus/',views.aboutus),
    path('contectus/',views.contectus),
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('product/',views.product),
    path('signout/',views.signout),
    path('myprofile/',views.myprofile),
    path('mycart/',views.mycart),
    path('cartitems/',views.cartitems),
    path('myorder/',views.myorders),
    path('indexcart/',views.indexcart),
    path('orderlist/',views.orderlist),
    path('myinformation/',views.myinformation),

    path('',views.index),
]