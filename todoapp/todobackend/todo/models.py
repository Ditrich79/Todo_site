from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    memo = models.TextField(blank=True, verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created', )
        verbose_name = 'дело'
        verbose_name_plural = 'Дела'

