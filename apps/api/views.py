from rest_framework.views import APIView
from django.contrib.auth.models import User

from apps.api.serializers import UserSerializer


class GetUsers(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
