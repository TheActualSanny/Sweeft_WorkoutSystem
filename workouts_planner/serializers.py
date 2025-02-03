from rest_framework import serializers
from .models import WorkoutPlans, WorkoutInstances
from workouts_main.models import DefinedWorkouts

class WorkoutSerializer(serializers.Serializer):
    '''
        The serializer that we will use in order to validate
        the data that the user sends in the post request.
    '''
    plan_name = serializers.CharField() 
    excercise = serializers.CharField()
    frequency = serializers.IntegerField()
    repetitions = serializers.IntegerField()
    sets = serializers.IntegerField()
    duration = serializers.IntegerField()
    distance = serializers.IntegerField()


    def validate(self, data):
        '''
            The main purpose of this is to check whether or not
            the workout with the passed name is actually defined in the PredefinedWorkouts
        '''

        excercise_name = data['excercise']
        defined = DefinedWorkouts.objects.filter(workout_name = excercise_name)
        if not defined:
            raise ValueError('This excercise is not defined!')
        elif WorkoutInstances.objects.filter(excercise = defined):
            raise ValueError('This workout is already added to the plan!')

        return data


class PlanSerializer(serializers.ModelSerializer):
    '''
        The serializer that we will use in order to validate
        the data that the user sends in the post request.
    '''

    class Meta:
        model = WorkoutPlans
        fields = ['plan_name', 'plan_type', 'daily_session_duration']

    def validate(self, data):
        '''
            The main purpose of this is to check whether or not
            the workout with the passed name is actually defined in the PredefinedWorkouts
        '''

        plan_name = data['plan_name']
        if WorkoutPlans.objects.filter(plan_name = plan_name):
            raise ValueError('This plan is already created!')
        return data
    