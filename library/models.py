import uuid

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


THEME_CHOICES = (
    ('architecture', 'ARCHITECTURE'),
    ('city', 'CITY'),
    ('classic', 'CLASSIC'),
    ('creator', 'CREATOR'),
    ('friends', 'FRIENDS'), 
    ('ideas', 'IDEAS'),
    ('art', 'ART'),
    ('education', 'EDUCATION'),
    ('mario', 'MARIO'),
    ('spider-man', 'SPIDER_MAN'),
)
def_image = "https://res.cloudinary.com/drs3eqnpf/image/upload/v1673709187/BrickLib/default_zp429f.jpg"


class Set (models.Model):
    """Django database model for add new set"""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name='user_sets')
    name = models.CharField(max_length=50, blank=False, null=True)
    theme = models.CharField(max_length=12, choices=THEME_CHOICES, blank=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    done = models.BooleanField(default=False)
    featured_image = CloudinaryField('image', default=def_image)
    likes = models.ManyToManyField(User, related_name='set_likes', blank=True)
    created_on = models.DateTimeField(auto_now=True)
    

def __str__(self):
    return self.theme
   
   
def number_of_likes(self):
    return self.likes.count()
    