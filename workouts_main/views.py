from django.shortcuts import render, HttpResponse, redirect
from .models import DefinedWorkouts
from .serializers import HomePageSerializer
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Views that make up the main website will be implemented here.

class HomePageAPI(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        '''
                The 20 pre-instantiated workout records will be returned by this endpoint,
                each one having short descriptions, instructions for execution, target muscles
                and additional info.

                The user can not add them to the workout plan from the home page. This will be possible via
                the customized_plan endpoint.
        '''
        defined_queryset = DefinedWorkouts.objects.all()
        serializer = HomePageSerializer(defined_queryset, many = True)
        return Response(serializer.data)
    
