from os import truncate
from typing import TYPE_CHECKING
from django.db import models
import uuid

# Create your models here.

# python manage.py makemigrations => to migrate classes
# python manage.py migrate => database refreshment

#Notice that in Project class tags variable has a stiring 'Tag' paramateter beucase Tag class is below Pject class if Tag class was above Project class then it we dont need to put string around it. 
# blank=True is telling Django that it is ok i=the field is empty.

class Project(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags=models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.title
    
#  VOTE_TYPE is a tuple the first value is tage and the second is a choice and choice is an attribute. see value variable in class Review
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up vote'),
        ('down', 'Down vote')
    )
    # owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio=  models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.value
    
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    