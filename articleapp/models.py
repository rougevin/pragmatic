from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article')

    title = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)
    create_at = models.DateField(auto_created=True, null=True)
