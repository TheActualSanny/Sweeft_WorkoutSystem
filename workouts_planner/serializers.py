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
    frequency = serializers.IntegerField(required = False, allow_null = True)
    repetitions = serializers.IntegerField(required = False, allow_null = True)
    sets = serializers.IntegerField(required = False, allow_null = True)
    duration = serializers.IntegerField(required = False, allow_null = True)
    distance = serializers.IntegerField(required = False, allow_null = True)


    def validate(self, data):
        '''
            The main purpose of this is to check whether or not
            the workout with the passed name is actually defined in the PredefinedWorkouts
        '''
        target_plan = data['plan_name']
        excercise_name = data['excercise']
        defined = DefinedWorkouts.objects.filter(workout_name = excercise_name)

        plan = WorkoutPlans.objects.filter(plan_name = target_plan)
        if not plan:
            raise ValueError('The plan that you passed does not exist!')
        if not defined:
            raise ValueError('This excercise is not defined!')
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
    