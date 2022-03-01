from django.contrib import admin

# Register your models here.

from .models import Class, Artist

admin.site.register(Class)
admin.site.register(Artist)