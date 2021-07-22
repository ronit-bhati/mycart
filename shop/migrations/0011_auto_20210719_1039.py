# Generated by Django 3.2.4 on 2021-07-19 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20210719_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]