from django.contrib.auth.models import User
from django.db import models

class DefinedWorkouts(models.Model):
    '''
        We define the table for pre-defined excercises.
    '''
    id = models.AutoField(primary_key = True)
    workout_name = models.CharField(max_length = 150)
    workout_instruction = models.CharField(max_length = 300)
    workout_description = models.CharField(max_length = 500)
    muscle_group = models.CharField(max_length = 50)
