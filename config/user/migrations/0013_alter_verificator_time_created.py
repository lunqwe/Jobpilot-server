# Generated by Django 5.0.1 on 2024-01-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_verificator_delete_emailverificator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificator',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
