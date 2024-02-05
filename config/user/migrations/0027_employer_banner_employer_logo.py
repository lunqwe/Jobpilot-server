# Generated by Django 5.0.1 on 2024-02-05 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_remove_employer_banner_remove_employer_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='media/banners'),
        ),
        migrations.AddField(
            model_name='employer',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/logo'),
        ),
    ]
