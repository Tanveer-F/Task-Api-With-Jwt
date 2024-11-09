from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('auth/', include('rest_framework.urls')), # Add this line for login/logout
]
