# Generated by Django 5.0.1 on 2024-03-05 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0008_rename_author_vacancy_employer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='vaсancies',
            new_name='vacancies',
        ),
    ]
