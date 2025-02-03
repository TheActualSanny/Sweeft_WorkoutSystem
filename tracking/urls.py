from . import views
from django.urls import path

app_name = 'tracking'

urlpatterns = [
    path('fitnesstracking/', views.FitnessTracking.as_view(), name = 'tracking')
]
