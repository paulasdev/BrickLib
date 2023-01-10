import datetime

from django.db import models
from django.utils.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class bricks (models.Model):
    id = models.ForeignKey(User, on_delete=models.CASCADE)
    pcs = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=200)
    is_built = models.BooleanField(default=False)
    set_number = models.IntegerField(default=0)
   
   
def __str__(self):
    return self.set_number
    