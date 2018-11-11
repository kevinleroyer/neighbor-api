from django.contrib import admin
from django.contrib.auth import get_user_model

from apps.accounts.models import Skill, SkillsCategory


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    fieldsets = (
        ('User info', {
            'fields': ('picture', 'username', 'first_name', 'last_name', 'email')
        }),
        ('User skills', {
            'fields': ('skills',)
        }),
        ('Address info', {
            'fields': ('address1', 'address2', 'zip_code', 'state', 'country')
        }),
        ('User status', {
            'fields': ('is_active', 'is_superuser', 'is_staff')
        }),
    )


admin.site.register(get_user_model(), UserAdmin)
admin.site.register(SkillsCategory)
admin.site.register(Skill)
