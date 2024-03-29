# Generated by Django 5.0.1 on 2024-02-22 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0039_alter_candidate_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='banner',
            field=models.ImageField(blank=True, default='default_icon.png', upload_to='employer/banners'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='logo',
            field=models.ImageField(blank=True, default='default_icon.png', upload_to='employer/logo'),
        ),
    ]
