''' The serializer. for the view responsible for excercise tracking and setting goals will be 
implemented here '''
from rest_framework import serializers
from workouts_main.models import DefinedWorkouts

class TrackingSerializer(serializers.Serializer):
    excercise = serializers.CharField()
    weight = serializers.IntegerField()
    weight_objective = serializers.IntegerField()
    goal = serializers.CharField()
    achievement = serializers.CharField()
    
    def validate(self, data):
        '''
            We check if the excercise that the user passed is into the defined excercises' table or not.
            If it isn't, it raises a ValueError exception.
        '''
        try:
            DefinedWorkouts.objects.get(workout_name = data.get('excercise'))
        except DefinedWorkouts.DoesNotExist:
            raise ValueError('The excercise is not in the defined table!')
        return data