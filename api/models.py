from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

"""
The email is used as a username for authentication
"""
class User(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True)
    email = models.EmailField(_('email address'), unique = True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
        return '{}'.format(self.email)


"""
UserProfile has an extra fields and has an one to one relationship with User model
"""
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'profile')
    host = models.BooleanField(default=False)
    location = models.CharField(max_length=120, blank=False, default='bogota')
    description = models.TextField(blank=True)
    phone = models.PositiveIntegerField(blank=True, default=1112223344)
    active = models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to = 'uploads', blank = True)
    
