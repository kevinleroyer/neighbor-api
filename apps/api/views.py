from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.accounts.models import Skill, SkillsCategory
from .serializers import UserSerializer, SkillSerializer, SkillsCategorySerializer


class SkillsCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows skills categories to be viewed or edited.
    """
    queryset = SkillsCategory.objects.all()
    serializer_class = SkillsCategorySerializer
    permission_classes = (IsAuthenticated,)


class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows skills to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAuthenticated,)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
