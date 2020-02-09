from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns = [

   url('^$' , views.index , name = 'home'),
   url('show/' , views.show , name = 'show'),
   url('details/(?P<id>[\d]*)/',views.details , name="details"),
]
