# Generated by Django 4.2.4 on 2023-09-09 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0020_remove_major_popularity'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='description',
            field=models.TextField(default='Информация об факультете', null=True, verbose_name='Описание факультета'),
        ),
        migrations.AddField(
            model_name='major',
            name='img',
            field=models.ImageField(default='location/default_image.png', upload_to='majors/images', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='major',
            name='popularity',
            field=models.BooleanField(default=False, verbose_name='Популярный факультет'),
        ),
    ]
