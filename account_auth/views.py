import requests
from .models import BlackListedTokens
from .authenticate import IsTokenValid
from .serializers import UserRegisterSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class RegisterAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        '''
            This will create a new user instance and will call the "/api/token/" endpoint in order to get
            the access/refresh tokens for the user. As a response,
            this will return:

            username: The username of the registered account.
            password: The password of the registered account.
            access_token and refresh_token: Both will be fetched calling the TokenObtainPerView method.
        '''

        serializer = UserRegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        try:
            user = User.objects.create_user(username = request.data.get('username'), password = request.data.get('password'))
            refresh_token = RefreshToken.for_user(user)
            access_token = str(refresh_token.access_token)
            
        except:
            raise ValueError("The user already exists!")
        return Response({**serializer.data, 'access' : access_token})
    

class LoginAPI(APIView):
    '''
        The implementation for the login process will be written here.
        For now, the API will just check the password strings.
        As I will implement hashing later on, this implementation will be modified.
    '''
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if authenticate(request, username = username, password = password):
            user = User.objects.filter(username = username).first()
            refresh_token = RefreshToken.for_user(user)
            access_token = str(refresh_token.access_token)
        else:
            raise AuthenticationFailed('Make sure to input correct user credentials!')
        # return Response({'error' : 'Incorrect user credentials!'})
        return Response({'message' : 'Successfully logged in!', 'access' : access_token})
    
class LogoutAPI(APIView):
    '''
        This view will handle logging out the user.
        To do this, the token will simply be blacklisted.
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
        return Response({'message' : 'Successfully logged out!'})



# @csrf_exempt
# def register_view(request):        
#     '''
#             We will instantiate a form object, validate the data and set the JWT tokens
#             and redirect the user to the home page of the workout planner, which will
#             display all of the 20 added workouts.

#             For now, this fetches the tokens via sending a get request to the TokenObtainPerView view, will change 
#             the implementation.
#     '''
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         finalized_form = ...
#         if finalized_form.is_valid():
#             user = User.objects.create_user(username = username, password = password)
#             refresh_token = RefreshToken.for_user(user)
#             access_token = str(refresh_token.access_token)
#             home_redirect = redirect('workouts_main:home')
#             home_redirect.set_cookie('access_token', access_token, httponly = True, expires = 120)                
#             home_redirect.set_cookie('refresh_token', str(refresh_token), httponly = True, expires = 500)

#             return home_redirect
#         else:
#             return HttpResponse('User registration failed!')
#     else:
#         empty_form = ...
#         return render(request, 'account_auth/register_page.html', context = {'register_form' : empty_form})

# @csrf_exempt
# def login_view(request):
#     '''
#         This will be called whenever a user logs into the account.
#         Just like the register_view, we will utilize JWT tokens.
#         We first call the authenticate() method that Django provides out of the box,
#         and then we get new RefreshToken values for the user
#     '''
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         potential_user = authenticate(username = username, password = password)

#         if potential_user:
#             refresh_token = RefreshToken.for_user(potential_user)
#             access_token = str(refresh_token.access_token)
#             home_redirect = redirect('workouts_main:home')
#             home_redirect.set_cookie('access_token', access_token, httponly = True, expires = 120)                
#             home_redirect.set_cookie('refresh_token', str(refresh_token), httponly = True, expires = 500)            
#             return home_redirect
#         else:
#             messages.error(request, message = 'Please input correct user credentials!')
#     return render(request, 'account_auth/login_page.html')