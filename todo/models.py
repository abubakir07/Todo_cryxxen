from django.db import models

from django.core.validators import RegexValidator


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(
        regex=r"^\+996\d{9}$",
        message="Phone number must be entered in the format: '+996123456789'."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
    

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='tasks', blank=True, null=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title