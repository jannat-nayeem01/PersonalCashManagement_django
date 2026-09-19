from . import views
from django.urls import path

urlpatterns = [
  
    path('',views.registration,name='registration'),
    path('login/',views.loginview,name='loginview'),
    path('profile/',views.profile,name='profile'),
    path('transaction/',views.transaction,name='transaction'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout/',views.logoutview,name='logoutview')
    
]
