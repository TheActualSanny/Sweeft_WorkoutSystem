# Generated by Django 5.1.5 on 2025-02-03 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts_planner', '0003_workoutinstances_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workoutplans',
            old_name='daily_session',
            new_name='daily_session_duration',
        ),
    ]
