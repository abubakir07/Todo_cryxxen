from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(
        regex=r"^\+996\d{9}$",
        message="Phone number must be entered in the format: '+996123456789'."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = 'Users'


