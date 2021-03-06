# Generated by Django 3.0 on 2020-02-27 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20200211_1457'),
        ('home', '0002_store_items_description'),
        ('orders', '0003_auto_20200225_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='buyerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.SignUser'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='itemId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Store_items'),
        ),
    ]
