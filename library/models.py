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


class Set (models.Model):
    """Django database model for add new set"""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    author = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            null=False,
                            blank=False,
                            related_name='user_sets')
    theme = models.CharField(max_length=12, choices=THEME_CHOICES, 
                            default='none')
    pcs = models.IntegerField()
    description = models.TextField()
    is_built = models.BooleanField(default=False)
    set_number = models.IntegerField()
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='set_likes', blank=True)
    created_on = models.DateTimeField(auto_now=True)
    
    

def __str__(self):
    return self.theme
   
   
def number_of_likes(self):
    return self.likes.count()
    