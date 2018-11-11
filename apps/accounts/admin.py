from django.contrib import admin
from django.contrib.auth import get_user_model

from apps.accounts.models import Skill, SkillsCategory

admin.site.register(get_user_model())
admin.site.register(SkillsCategory)
admin.site.register(Skill)

