# Generated by Django 3.2.13 on 2022-06-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='this is cool!'),
        ),
    ]
