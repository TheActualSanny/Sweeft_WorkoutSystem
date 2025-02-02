from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'account_auth'

urlpatterns = [
    path('register/', views.RegisterAPI.as_view(), name = 'register'),
    path('login/', views.LoginAPI.as_view(), name = 'login'),
    path('logout/', views.LogoutAPI.as_view(), name = 'logout'),
    path('api/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
]