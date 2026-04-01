from django.db import models
from tinymce.models import HTMLField


# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField(blank=True, null=True)
    notice_date = models.DateField()
    
    
    def __str__(self):
        return self.title
    
    
class Event(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateField()
    details = HTMLField(blank=True, null=True)
    
    
    def __str__(self):
        return self.name   