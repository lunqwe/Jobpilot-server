# Generated by Django 5.0.1 on 2024-03-05 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0009_rename_vaсancies_vacancy_vacancies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='vacancies',
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='expiration_date',
            field=models.CharField(default='', max_length=255),
        ),
    ]
