# Generated by Django 4.0 on 2021-12-19 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_apscheduler', '0008_remove_djangojobexecution_started'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='djangojobexecution',
            constraint=models.UniqueConstraint(fields=('job_id', 'run_time'), name='unique_job_executions'),
        ),
    ]
