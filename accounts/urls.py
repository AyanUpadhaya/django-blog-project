# accounts urls file


from django.urls import path, include
from . views import *
urlpatterns = [

    path('register',userRegistration,name='register'),
    path('login',userLogin,name='login'),
    path('logout',userLogout,name='logout')
]
