# Generated by Django 4.2.4 on 2023-09-02 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0017_alter_review_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
