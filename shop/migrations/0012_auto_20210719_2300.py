# Generated by Django 3.2.4 on 2021-07-19 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20210719_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
