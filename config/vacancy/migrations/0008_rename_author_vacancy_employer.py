# Generated by Django 5.0.1 on 2024-03-02 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0007_alter_vacancy_author_alter_vacancy_candidates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='author',
            new_name='employer',
        ),
    ]