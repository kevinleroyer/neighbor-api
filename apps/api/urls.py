from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='user')
router.register('skills/categories', views.SkillsCategoryViewSet, basename='skills-category')
router.register('skills', views.SkillViewSet, basename='skill')

urlpatterns = router.urls
urlpatterns += [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]