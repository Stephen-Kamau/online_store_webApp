from django.conf.urls import url , include
from . import views


app_name = "orders"
urlpatterns = [
    url('^$' , views.orders , name="ordersGoods"),
    url("cart/delete/" , views.delete , name="delete"),
     url('cart/' , views.displayCart , name="displayCart"),
     url('buy/' , views.buy , name="buyGoods"),
]
