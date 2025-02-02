from django.db import models
from django.contrib.auth.models import User
from workouts_main.models import DefinedWorkouts

class WorkoutPlans(models.Model):
    '''
        This model will be used to store data about 
        the custom workout plans that the user creates.
    '''
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    plan_name = models.CharField(max_length = 150)
    plan_type = models.CharField(max_length = 50)
    daily_session = models.IntegerField(null = True)

class WorkoutInstances(models.Model):
    '''
        These will be the individual workout instances that will be added to the
        workout plans. They will have  foreign keys to the corresponding predefined workout,
        but they will also have addition fields like duration, sets, repetitions, distance..
    '''
    workout_plan = models.ForeignKey(WorkoutPlans, on_delete = models.CASCADE)
    excercise = models.ForeignKey(DefinedWorkouts, on_delete = models.CASCADE)
    frequency = models.IntegerField(null = True)
    repetitions = models.IntegerField(null = True)
    sets = models.IntegerField(null = True)
    duration = models.IntegerField(null = True)
    distance = models.IntegerField(null = True)