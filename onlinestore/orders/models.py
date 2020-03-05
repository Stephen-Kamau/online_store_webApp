from django.db import models
from home.views import Store_items
from signup.views import SignUser

# Create your models here.
class OrderItems(models.Model):
    orderId = models.AutoField(primary_key=True)
    ownerEmail = models.EmailField(max_length = 50)
    itemId = models.ForeignKey(Store_items , on_delete = models.CASCADE)
    buyerId = models.ForeignKey(SignUser , on_delete = models.CASCADE)
    price = models.IntegerField()
    # itemTitle = models.CharField(max_length = 50)
    # BuiltType = models.CharField(max_length = 50)
    # ownerPhone = models.CharField(max_length = 50)
    # pic = models.ImageField(max_length = 100 , default = "None")
    # post_time = models.DateTimeField(auto_now_add=True)
    # bought_status = models.BooleanField(default = False , max_length = 3)
    # description = models.CharField(max_length = 200)

    class Meta:
        db_table = "OrderItems"
