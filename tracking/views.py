from .serializers import TrackingSerializer
from .models import TrackWorkouts
from account_auth.authenticate import IsTokenValid
from workouts_main.models import DefinedWorkouts
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import responses


class FitnessTracking(APIView):
    '''
        This view will be responsible for not only tracking weight and progess, but also inserting goals for excercises.
        
    '''
    permission_classes = [IsAuthenticated, IsTokenValid]

    @swagger_auto_schema(request_body = TrackingSerializer, responses = {201 : TrackingSerializer})
    def post(self, request):
        serializer = TrackingSerializer(data = request.data)
        if serializer.is_valid():
            excercise = DefinedWorkouts.objects.get(workout_name = serializer.validated_data.get('excercise'))
            TrackWorkouts.objects.create(user = request.user, weight = serializer.validated_data.get('weight'),
                                        weight_objective = serializer.validated_data.get('weight_objective'),
                                        goal = serializer.validated_data.get('goal'), achievement = serializer.validated_data.get('achievement'),
                                        excercise = excercise
                                        )
            return Response({'mesage' : 'Successfully added a tracking instance!'})
        else:
            return Response({'message' : 'There was an error while trying to insert the data.'})
            
