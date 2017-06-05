from django.db import models
import uuid


class User(models.Model):
    email = models.EmailField(primary_key=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True


class Token(models.Model):
    uid = models.CharField(default=uuid.uuid4, max_length=40)
    email = models.EmailField()
