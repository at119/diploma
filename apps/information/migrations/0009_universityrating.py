# Generated by Django 4.2.4 on 2023-09-01 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0008_remove_university_professor_remove_university_text_p_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.university')),
            ],
        ),
    ]