from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group
from phonenumber_field.modelfields import PhoneNumberField

# user profile
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='users/%Y/%m/%d/', default='images/default-profile-image.jpeg', blank=True, null=True)
    phone_number = PhoneNumberField(blank=True)
    country = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    # created = 


    def __str__(self):
        return f' {self.user.username}'
    

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=True)
    description = models.TextField(null=True, blank=True)
    project_image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
class Bio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.user}'

class Skill(models.Model):
    user_bio = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'