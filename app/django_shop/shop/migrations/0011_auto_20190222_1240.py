# Generated by Django 2.1.7 on 2019-02-22 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20190222_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='shop.CartItem'),
        ),
    ]