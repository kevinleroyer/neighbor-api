from django.urls import path
from django.conf.urls import include

from .views import GetUsers

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', GetUsers.as_view(), name='get_users'),
]
