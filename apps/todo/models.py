from django.db import models

from apps.user.models import User    


class Todo(models.Model):
    
    title = models.CharField(
        max_length=200,
        verbose_name='title',
        unique=True
    )
    description = models.TextField(
        verbose_name='description'
    )
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at'
    )
    image = models.ImageField(
        upload_to='todo_img/',
        verbose_name='image',
        blank=True,
        null=True
    )
    owner=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner',
        verbose_name='owner',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return f'{self.id}---{self.title}'