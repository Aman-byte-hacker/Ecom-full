# Generated by Django 3.1.5 on 2021-11-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='mobile',
            field=models.IntegerField(default=0),
        ),
    ]
