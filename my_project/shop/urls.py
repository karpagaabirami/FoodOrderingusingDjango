from django.urls import path
from .import views
urlpatterns =[
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('collections',views.collections,name="collections"),
    path('collec/<int:pk>',views.collectionparticualr,name="collection1"),
    path('custo',views.customer,name='cuso'),
    path('login',views.custlogin,name='login'),
    path('logout',views.ulog,name='logout'),

]