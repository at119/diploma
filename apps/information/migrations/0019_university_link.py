# Generated by Django 4.2.4 on 2023-09-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0018_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='link',
            field=models.URLField(default='https://example.com'),
        ),
    ]