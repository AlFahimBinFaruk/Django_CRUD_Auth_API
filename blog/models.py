from django.db import models
from account.models import User

# blog model
class Blog(models.Model):
    blogger = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=333)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.CharField(max_length=333,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title