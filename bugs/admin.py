from django.contrib import admin
from .models import bug_item, BugComment
# Register your models here.

admin.site.register(bug_item)
admin.site.register(BugComment)