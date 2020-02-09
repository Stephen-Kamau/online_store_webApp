# Generated by Django 3.0 on 2020-02-09 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store_items',
            fields=[
                ('itemId', models.AutoField(primary_key=True, serialize=False)),
                ('ownerEmail', models.EmailField(max_length=50)),
                ('itemTitle', models.CharField(max_length=50)),
                ('BuiltType', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('ownerPhone', models.CharField(max_length=50)),
                ('pic', models.ImageField(default='None', upload_to='')),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('bought_status', models.BooleanField(default=False, max_length=3)),
            ],
            options={
                'db_table': 'Store_items',
            },
        ),
    ]