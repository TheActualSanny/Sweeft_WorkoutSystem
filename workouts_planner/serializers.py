from rest_framework import serializers
from .models import WorkoutPlans, WorkoutInstances
from workouts_main.models import DefinedWorkouts

class WorkoutSerializer(serializers.Serializer):
    '''
        The serializer that we will use in order to validate
        the data that the user sends in the post request.
    '''

    # class Meta:
        # fields = ['workout_plan', '']

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
    


    #  workout_plan = models.ForeignKey(WorkoutPlans, on_delete = models.CASCADE)
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
    # excercise = models.ForeignKey(DefinedWorkouts, on_delete = models.CASCADE)
    # frequency = models.IntegerField(null = True) # This must be a WorkoutPlans field
    # repetitions = models.IntegerField(null = True)
    # sets = models.IntegerField(null = True)
    # duration = models.IntegerField(null = True)
    # distance = models.IntegerField(null = True)

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
    