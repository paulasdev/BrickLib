import uuid

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


THEME_CHOICES = (
    ('Architecture', 'ARCHITECTURE'),
    ('City', 'CITY'),
    ('Classic', 'CLASSIC'),
    ('Creator', 'CREATOR'),
    ('Friends', 'FRIENDS'), 
    ('Ideas', 'IDEAS'),
    ('Art', 'ART'),
    ('Education', 'EDUCATION'),
    ('Mario', 'MARIO'),
    ('Spider-man', 'SPIDER_MAN'),
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
                               related_name="user_sets")
    title = models.CharField(max_length=50, null=True)
    theme = models.CharField(max_length=12, choices=THEME_CHOICES, blank=True)
    description = models.TextField()
    done = models.BooleanField(default=False)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now=True)
    

class Meta: 
    ordering = ['-created_on']


def __str__(self):
    return self.name
   
   
    