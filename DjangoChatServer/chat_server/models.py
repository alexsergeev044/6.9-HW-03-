from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Room(models.Model):

    objects = None
    name = models.CharField(max_length=256, unique=True)
    app_label = 'chat_server'


def user_list():
    users = UserProfile.objects.filter().order_by('name')
    # users = "qwerty"
    return list(users)


class UserProfile(models.Model):
    name = models.CharField(max_length=256, unique=True)
    avatar = ThumbnailerImageField(resize_source={'size': (300, 300), 'crop': 'smart'}, upload_to='djangochatserver', default='djangochatserver/default.jpg')
    avatar_small = ThumbnailerImageField(resize_source={'size': (30, 30), 'crop': 'smart'}, upload_to='djangochatserver', default='djangochatserver/default_small.jpg')
    room = models.OneToOneField(Room, on_delete=models.SET_NULL, null=True)
    online = models.BooleanField(default=False)


class Message(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
