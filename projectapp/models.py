from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Project(models.Model):
    opener = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project')
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} : {self.title}'
