from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url('admin/', admin.site.urls),
    url('' ,include('home.urls')),
    url('signup/' ,include('signup.urls')),
    url('login/' ,include('login.urls')),
    url('orders/' ,include('orders.urls')),
    # url('show/' , include('error.urls')),
] +static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
