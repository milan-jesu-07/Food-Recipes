from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='media/images', default="")
    bio = models.CharField(max_length=120)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return str(self.user)
