from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import Skill, SkillsCategory, User
from .serializers import UserSerializer, SkillSerializer, SkillsCategorySerializer


class SkillsCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows skills categories to be viewed or edited.
    """
    queryset = SkillsCategory.objects.all()
    serializer_class = SkillsCategorySerializer


class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows skills to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserSkillsViewSet(APIView):
    """
    API endpoint that allows users with a particular skill to be viewed.
    """
    def get(self, request, skill_id):
        users = User.objects.filter(skills=skill_id)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
