# Generated by Django 5.0.1 on 2024-02-03 00:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_candidate_expire_candidate_five_job_alerts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='profile_privasy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='candidate',
            name='resume_privasy',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='CandidateJobAlertNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.candidate')),
            ],
        ),
    ]
