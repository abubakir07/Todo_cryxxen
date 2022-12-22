from django.db import models

from apps.user.models import User    


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='todos', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='User')

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return self.title