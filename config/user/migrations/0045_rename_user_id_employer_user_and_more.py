# Generated by Django 5.0.1 on 2024-03-03 21:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0044_alter_employer_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employer',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='user_id',
        ),
        migrations.AddField(
            model_name='candidate',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='candidate', related_query_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]