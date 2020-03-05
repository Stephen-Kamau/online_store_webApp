from django.conf.urls import url , include
from django.urls import path
from . import views

app_name = "login"

urlpatterns = [

     url('' , views.login , name="login"),
     url('logout$' , views.login , name="signout"),
]
