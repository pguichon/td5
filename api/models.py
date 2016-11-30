from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, null=True)
    titre = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
