from django.contrib import admin

from .models import Category, Content, SidePicture

# Register your models here.
admin.site.register(Category)
admin.site.register(Content)
admin.site.register(SidePicture)

