# Generated by Django 3.1.7 on 2021-04-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Module', '0006_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='', upload_to='products/images'),
        ),
    ]