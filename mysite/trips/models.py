from django.conf import settings
from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    traveled_at = models.DateField(auto_now_add=True, default=datetime.now())
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)

class Auth():

    def create_user(self, first_name, last_name, email, pwd):
        user = User.objects.create_user(first_name, email, pwd)

        # At this point, user is a User object that has already been saved
        # to the database. You can continue to change its attributes
        # if you want to change other fields.
        user.last_name = last_name
        user.save()

    def change_password(self, first_name, pwd):
        user = User.objects.get(username=first_name)
        user.set_password(pwd)
        user.save()

    def authenticate(self, first_name, pwd):
        user = authenticate(username=first_name, password=pwd)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                return "Welcome back %s! :)" % (first_name)
            else:
                return "Please contact Administrator, your account has been disabled!"
        else:
            return "The username and password were incorrect."
