# Generated by Django 5.0.1 on 2024-02-01 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_alter_employersociallink_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
