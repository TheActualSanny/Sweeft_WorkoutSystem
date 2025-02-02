from . import views
from django.urls import path

app_name = 'workout_planner'

urlpatterns = [
    path('create/', views.CreateWorkoutPlan.as_view(), name = 'create'),
    path('add/', views.AddWorkoutExcercise.as_view(), name = 'add')
]