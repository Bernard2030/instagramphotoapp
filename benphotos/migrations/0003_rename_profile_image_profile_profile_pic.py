# Generated by Django 3.2.8 on 2021-10-19 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benphotos', '0002_comment_followers_image_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_image',
            new_name='profile_pic',
        ),
    ]
