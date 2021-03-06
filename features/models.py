from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=254, default="")
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    value_collected = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    target_value = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class FeatureContributors(models.Model):
    user = models.ForeignKey(User, null=True)
    amount = models.CharField(max_length=254, default="")
    date_contributed = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Feature, null=True)


class FeatureViews(models.Model):
    user = models.ForeignKey(User, null=True)
    post = models.ForeignKey(Feature, null=True)

    def __str__(self):
        return self.name
