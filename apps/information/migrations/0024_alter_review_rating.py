# Generated by Django 4.2.4 on 2023-09-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0023_famouspeople_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
