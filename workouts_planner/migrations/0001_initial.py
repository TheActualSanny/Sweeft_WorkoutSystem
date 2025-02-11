# Generated by Django 5.1.5 on 2025-02-02 01:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workouts_main', '0002_auto_20250131_2335'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutPlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=150)),
                ('plan_type', models.CharField(max_length=50)),
                ('daily_session', models.IntegerField()),
                ('frequency', models.IntegerField()),
                ('excercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts_main.definedworkouts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
