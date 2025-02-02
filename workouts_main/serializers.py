''' The serializers for the main workouts API will be implemented here.  '''
from rest_framework.serializers import Serializer, ModelSerializer
from .models import DefinedWorkouts

class HomePageSerializer(ModelSerializer):
    ''' The class which will serialize the defined excercises' data in a JSON format, which will
        then be returned as a Response object. 
    '''
    class Meta:
        model = DefinedWorkouts
        fields = ['workout_name', 'workout_instruction', 'workout_description', 'muscle_group']