from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema = get_schema_view(
    openapi.Info(title = 'Workouts Manager', default_version = '1.0.0', 
                 description =  'The documentation of the personalized workouts API'),
    public = True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', schema.with_ui('swagger', cache_timeout = 0), name = 'documentation'),
    path('', include('account_auth.urls'), name = 'AUTH'),
    path('home/', include('workouts_main.urls')),
    path('plans/', include('workouts_planner.urls')),
    path('tracking/', include('tracking.urls'))
]
