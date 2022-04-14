from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Park(models.Model):
    name = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    size = models.IntegerField()
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']