# Generated by Django 3.0 on 2020-02-25 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='itemId',
            field=models.IntegerField(max_length=30),
        ),
    ]
