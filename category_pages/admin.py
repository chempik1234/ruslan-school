from django.contrib import admin

from .models import Category, Content, SidePicture
from .forms import ContentAdminForm


class ContentAdmin(admin.ModelAdmin):
    form = ContentAdminForm


# Register your models here.
admin.site.register(Category)
admin.site.register(Content)   # , ContentAdmin)
admin.site.register(SidePicture)

