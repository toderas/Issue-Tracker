from django.db import models

# Create your models here.

class bug_item(models.Model):
    name = models.CharField(max_length=254, default="")
    description = models.TextField()
    in_progress = models.BooleanField(blank=False, default=False)
    
    def __str__(self):
        return self.name