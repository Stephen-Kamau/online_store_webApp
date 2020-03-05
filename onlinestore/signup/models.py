from django.db import models

# Create your models here.
class SignUser(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 60  , unique = True)
    fname = models.CharField(max_length = 60)
    lname = models.CharField(max_length = 60)
    email = models.EmailField(max_length = 60 , unique = True)
    password = models.CharField(max_length = 30)

    class Meta:
        db_table = "SignUser"
