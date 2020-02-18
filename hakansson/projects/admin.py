from django.contrib import admin

# Rel. Imports 
from .models import Project, Category, Tag

# Register your models here.
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Tag)