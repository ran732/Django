from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=200, default="")
    description = HTMLField(blank=True, null=True)
    notice_date = models.DateField(default=timezone.now)
    
    
    def __str__(self):
        return self.title
    
    
class Event(models.Model):
    name = models.CharField(max_length=200, default="")
    event_date = models.DateField(default=timezone.now)
    details = HTMLField(blank=True, null=True)
    
    
    def __str__(self):
        return self.name   
    

class Note(models.Model):

    SUBJECT_CHOICES = [
        ('math', 'Mathematics'),
        ('physics', 'Physics'),
        ('cs', 'Computer Science'),
    ]

    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)

    description = models.TextField(blank=True)

    file = models.FileField(upload_to='notes/', blank=True, null=True)

    drive_link = models.URLField(blank=True, null=True)

    content = HTMLField(blank=True, null=True)  # TinyMCE text notes

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    