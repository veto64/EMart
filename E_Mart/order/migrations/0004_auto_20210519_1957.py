# Generated by Django 3.1.7 on 2021-05-19 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210519_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='is_delivered',
            field=models.BooleanField(default=False, verbose_name='status'),
        ),
    ]