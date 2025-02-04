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
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class CreateWorkoutPlan(APIView):
    '''
        View managing for creating workout plans.
        Each record will have a foreign key which will connect it to the current user.
        The actual excercises however are stored in a seperate WorkoutInstances model,
        and each workout will have 3 foreign keys: User, Plan and Defined Workout
    '''
    permission_classes = [IsAuthenticated, IsTokenValid]
    
    @swagger_auto_schema(request_body = PlanSerializer)
    def post(self, request):
        serializer = PlanSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        validated = serializer.validated_data
        name = validated.get('plan_name')
        WorkoutPlans.objects.create(user = request.user, plan_name = validated.get('plan_name'),
                                    plan_type = validated.get('plan_type'), daily_session_duration = validated.get('daily_session'))
        return Response({'message' : f'successfully created plan: {name}'})
    
class AddWorkoutExcercise(APIView):
    '''
        This view will be ujsed to insert excercise instances into our plans.
        This will have additional validation to ensure that the workout plan that we are dealing with
        is related to the current user.
    '''
    permission_classes = [IsAuthenticated, IsTokenValid]

    @swagger_auto_schema(request_body = WorkoutSerializer)
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
        if not plan:
            return Response({'message' : f'Plan {plan_name} doesnt exist!'})
        else:
            already_exists = bool(WorkoutInstances.objects.filter(user = request.user).
                                  filter(workout_plan = plan).filter(excercise = chosen_excercise))
            WorkoutInstances.objects.create(user = request.user, workout_plan = plan, excercise = chosen_excercise,
                                            frequency = request.data.get('frequency'), repetitions = request.data.get('repetitions'),
                                            sets = request.data.get('sets'), duration = request.data.get('duration'),
                                            distance = request.data.get('distance'))
            return Response({'message' : 'Successfully added the new excercise!'})
        
class CustomizeWorkoutExcercise(APIView):
    '''
        This view will handle the modification of  excercises that the user added to the class.
        For now, the user will pass in an id of the excercise that must be changed, and any new
        field values.
    '''
    permission_classes = [IsAuthenticated, IsTokenValid]

    @swagger_auto_schema(request_body = openapi.Schema(
                type = openapi.TYPE_OBJECT,
                required = ['target_plan', 'target_excercise'],
                properties = {
                    'plan_name': openapi.Schema(type = openapi.TYPE_STRING, description = 'The plan which the excerise is added to'),
                    'excercise': openapi.Schema(type = openapi.TYPE_STRING, description = 'The excercise itself'),
                    'target_fields' : openapi.Schema(type = openapi.TYPE_STRING, description = '''Optional: pass any of the fields
                    and values that you wish to update them to as kwargs.''')
                },
            ))

    def post(self, request):
        '''
            Considering that each plan will have a single instance of a workout, 
            we simply get that workout excercise.
            It will then parse the request.data and update the existing fields with the passed values.
            This implementation is dynamic, meaning that it makes it possible for the user to pass in any ammount of JSON key-value 
            pairs to modify the target excercise.
        '''
        
        serializer = WorkoutSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            plan = WorkoutPlans.objects.get(plan_name = serializer.validated_data.get('plan_name'))
            target_excercise = DefinedWorkouts.objects.get(workout_name = serializer.validated_data.get('excercise'))
            curr_instances = WorkoutInstances.objects.filter(user = request.user).filter(workout_plan = plan)
            target = curr_instances.get(excercise = target_excercise)    
            model_keys = [i.name for i in WorkoutInstances._meta.fields]
            data = {field_name : serializer.validated_data.get(field_name) for field_name, field in serializer.fields.items() if not field.required}
            for param in data:
                if param in model_keys:
                    setattr(target, param, data[param])
            target.save()
            return Response({'message' : 'Successfully updated the excercise!'})
        else:
            return Response({'message' : 'Check the input fields'})
        

        
