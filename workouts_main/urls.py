from . import views
from django.urls import path

app_name = 'workouts_main'

urlpatterns = [
    path('', views.HomePageAPI.as_view(), name = 'home')
]