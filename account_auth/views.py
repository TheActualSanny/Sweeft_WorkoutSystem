import requests
from .models import BlackListedTokens
from .authenticate import IsTokenValid
from rest_framework import status
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserRegisterSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class RegisterAPI(APIView):

    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=UserRegisterSerializer,
        responses={201: UserRegisterSerializer}
    )
    def post(self, request):
        '''
        This view will allow the user to register a new account.
        For now, an account only has username and password fields.
        If the request had valid parameters, the username and password and returned as well as an access token,
        which is essential for the user to access any of the other endpoints.
        '''

        serializer = UserRegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        try:
            user = User.objects.create_user(username = request.data.get('username'), password = request.data.get('password'))
            refresh_token = RefreshToken.for_user(user)
            access_token = str(refresh_token.access_token)
            
        except:
            raise ValueError('The user already exists!')
        return Response({**serializer.data, 'access' : access_token})
    

class LoginAPI(APIView):
    '''
        The view responsible for logging the user in.
        After inputting correct user credentials in the request body and sending a POST request,
        the API will return a sucess message and an access token. Authorize with this access token in order
        to send request to any of the other endpoints ( except register ).
    '''
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body = LoginSerializer)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if authenticate(request, username = username, password = password):
            user = User.objects.filter(username = username).first()
            refresh_token = RefreshToken.for_user(user)
            access_token = str(refresh_token.access_token)
        else:
            raise AuthenticationFailed('Make sure to input correct user credentials!')
        return Response({'message' : 'Successfully logged in!', 'access' : access_token}, status = status.HTTP_200_OK)
    
class LogoutAPI(APIView):
    '''
        This view will handle logging out the user.
        As it is impossible to just delete the access token, 
        it will simply be blacklisted instead.
    '''
    permission_classes = [IsAuthenticated, IsTokenValid]

    def post(self, request):
        '''
            This will fetch the current access token, decode it in order to
            get the user and then insert the given token to the BlackListedToken table.
        '''
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        BlackListedTokens.objects.create(user = request.user,
                                        token = token)
        return Response({'message' : 'Successfully logged out!'}, status = status.HTTP_200_OK)
