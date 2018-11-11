from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.accounts.models import Skill, SkillsCategory


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('pk', 'title', 'thumbnail')


class SkillsCategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)

    class Meta:
        model = SkillsCategory
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'
        extra_kwargs = {
            'skills': {'lookup_field': 'title'}
        }