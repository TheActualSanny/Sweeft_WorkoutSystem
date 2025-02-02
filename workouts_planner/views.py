'''
    Views for the workout planning are implemented here.
'''

from .serializers import WorkoutSerializer, PlanSerializer
from .models import WorkoutPlans, WorkoutInstances
from workouts_main.models import DefinedWorkouts
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import ValidationError
from account_auth.authenticate import IsTokenValid

class CreateWorkoutPlan(APIView):
    '''
        View managing the insertion of new excercises into the workout plans.
        Considering that each workout plan will have a name, even if it is the
        first record inside the database, the user just sets the desired workout_name.
        There will be a seperate view which will return a single workout plan based
        on the workout name that the user inputs.
    '''
    permission_classes = [IsAuthenticated, IsTokenValid]
    
    def post(self, request):
        serializer = PlanSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        validated = serializer.validated_data
        name = validated.get('plan_name')
        WorkoutPlans.objects.create(user = request.user, plan_name = validated.get('plan_name'),
                                    plan_type = validated.get('plan_type'), daily_session = validated.get('daily_session'))
        return Response({'message' : f'successfully created plan: {name}'})
    
class AddWorkoutExcercise(APIView):
    '''
        This view will be ujsed to insert excercise instances into our plans.
        This will have additional validation to ensure that the workout plan that we are dealing with
        is related to the current user.
    '''
    permission_classes = [IsAuthenticated, IsTokenValid]

    def post(self, request):
        '''
            Additional validation will be implemented in the serializer. For now, it isn't checked
            whether the given excercise is in the predifined list.
        '''
        plan_name = request.data.get('plan_name')
        user_plans = WorkoutPlans.objects.filter(user = request.user)
        chosen_excercise = DefinedWorkouts.objects.get(workout_name = request.data.get('excercise'))
        try:
            plan = user_plans.get(plan_name = plan_name) # This part will be written in the serializer
        except:
            plan = None
        print(type(plan))
        if not plan:
            return Response({'message' : f'Plan {plan_name} doesnt exist!'})
        else:
            WorkoutInstances.objects.create(workout_plan = plan, excercise = chosen_excercise,
                                            frequency = request.data.get('frequency'), repetitions = request.data.get('repetitions'),
                                            sets = request.data.get('sets'), duration = request.data.get('duration'),
                                            distance = request.data.get('distance'))
            return Response({'message' : 'Successfully added the new excercise!'})
        
            
