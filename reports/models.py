from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model
class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(
        max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True, null=True
    )

    def __str__(self):
        return self.username
