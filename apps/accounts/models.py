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
    first_name = models.CharField(_('First name'), max_length=30)
    last_name = models.CharField(_('Last name'), max_length=150)
    skills = models.ManyToManyField(Skill)
    picture = models.ImageField(_('Picture'), upload_to='users', blank=True, null=True)

    CANADA = 'ca'
    QUEBEC = 'qc'
    STATES_CHOICES = (
        (QUEBEC, _('Quebec')),
    )
    COUNTRIES_CHOICES = (
        (CANADA, _('Canada')),
    )
    address1 = models.CharField(_('Address'), max_length=255)
    address2 = models.CharField(_('Address 2'), max_length=255, blank=True)
    zip_code = models.CharField(_('Zip code'), max_length=30)
    state = models.CharField(_('State'), max_length=50, choices=STATES_CHOICES, default=QUEBEC)
    country = models.CharField(_('Country'), max_length=3, choices=COUNTRIES_CHOICES, default=CANADA)

    class Meta:
        ordering = ('date_joined',)
