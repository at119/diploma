# Generated by Django 4.2.4 on 2023-08-31 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0006_university_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='professor',
            field=models.CharField(default='Подробная имя профессора', max_length=255, verbose_name='Имя профессора'),
        ),
        migrations.AddField(
            model_name='university',
            name='text_p',
            field=models.TextField(default='Подробная информация о профессоре будет доступна здесь.', verbose_name='Информация об профессоре'),
        ),
    ]
