# Generated by Django 3.1.7 on 2021-03-30 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Module', '0005_auto_20210330_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_social_user',
            field=models.BooleanField(default=True),
        ),
    ]
