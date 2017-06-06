from django.db import models
from django.contrib import auth
import uuid

"""TODO
Don't know what tf this is
Will look it up later
"""
auth.signals.user_logged_in.disconnect(auth.models.update_last_login)


class User(models.Model):
    email = models.EmailField(primary_key=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True


class Token(models.Model):
    uid = models.CharField(default=uuid.uuid4, max_length=40)
    email = models.EmailField()
