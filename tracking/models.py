from django.db import models
from workouts_main.models import DefinedWorkouts 
from django.contrib.auth.models import User

class TrackWorkouts(models.Model):
    '''
        This model will store not only weight information, but user goals aswell.
        Every record will have a foreign key to the current user.     
    '''
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    excercise = models.ForeignKey(DefinedWorkouts, on_delete = models.CASCADE)
    weight = models.IntegerField()
    weight_objective = models.IntegerField(null = True)
    goal = models.CharField(null = True, max_length = 60)
    achievement = models.CharField(null = True, max_length = 60)
    date = models.DateField(auto_now = True)
