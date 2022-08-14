from django.contrib import admin

from .models import User

# custom user model
admin.site.register(User)
