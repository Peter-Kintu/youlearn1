# Generated by Django 4.2.6 on 2023-11-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learn', '0004_videoupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='default.png', upload_to='profile_pic'),
        ),
    ]
