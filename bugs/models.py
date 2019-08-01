from django.db import models

# Create your models here.

class bug_item(models.Model):
    name = models.CharField(max_length=254, default="")
    description = models.TextField()
    
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
        