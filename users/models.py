from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    #picture = models.ImageField(null=True, blank=True)
    web_url = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Profiles"
