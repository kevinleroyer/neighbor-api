from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class SkillsCategory(models.Model):
    title = models.CharField(_('title'), max_length=30)
    thumbnail = models.ImageField(upload_to='skills', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = _('Categories')


class Skill(models.Model):
    title = models.CharField(_('title'), max_length=30)
    category = models.ForeignKey(SkillsCategory, on_delete=models.CASCADE, related_name='skills')
    thumbnail = models.ImageField(upload_to='skills', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class User(AbstractUser):
    email = models.EmailField(_('Email'), max_length=255, unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=150)
    skills = models.ManyToManyField(Skill)

    class Meta:
        ordering = ('date_joined',)
