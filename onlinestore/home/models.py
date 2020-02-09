from django.db import models
# Create your models here.
class Store_items(models.Model):
    itemId = models.AutoField(primary_key=True)
    ownerEmail = models.EmailField(max_length = 50)
    itemTitle = models.CharField(max_length = 50)
    BuiltType = models.CharField(max_length = 50)
    price = models.IntegerField()
    ownerPhone = models.CharField(max_length = 50)
    pic = models.ImageField(max_length = 100 , default = "None")
    post_time = models.DateTimeField(auto_now_add=True)
    bought_status = models.BooleanField(default = False , max_length = 3)

    class Meta:
        db_table = "Store_items"
