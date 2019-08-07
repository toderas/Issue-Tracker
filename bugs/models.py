from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.



class bug_item(models.Model):
    name = models.CharField(max_length=254, default="")
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now_add=True)
    
    STATUS = (
        ('Pending-review','Pending Review'),
        ('In-progress','In Progress'),
        ('Resolved', 'Resolved'),
        )
    status = models.CharField(
             max_length=20,
             choices=STATUS,
             default='Pending-review'
             )
    def __str__(self):
        return self.name
        
class Like(models.Model):
    user = models.ForeignKey(User, null=True)
    post = models.ForeignKey(bug_item, null=True)
    
        
class Views(models.Model):
    user = models.ForeignKey(User, null=True)
    post = models.ForeignKey(bug_item, null=True)


class BugComment(models.Model):
    post = models.ForeignKey(bug_item, null=True)
    author = models.CharField(max_length=200)
    comment = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=True)

    def __str__(self):
        return self.comment