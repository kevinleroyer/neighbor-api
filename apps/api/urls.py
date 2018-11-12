from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('skills/categories', views.SkillsCategoryViewSet)
router.register('skills', views.SkillViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('users/skills/<int:skill_id>', views.UserSkillsViewSet.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]