from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account_auth.urls')),
    path('home/', include('workouts_main.urls')),
    path('plans/', include('workouts_planner.urls'))
]
