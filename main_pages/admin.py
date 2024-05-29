from django.contrib import admin
from django.forms import inlineformset_factory
from django.utils.html import format_html

from .forms import NewsAdminForm
from .models import News, NewsImage, SliderImage


class ImagePreviewWidget(admin.widgets.AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            output.append(format_html('<a href="{0}" target="_blank"><img src="{0}" style="max-width: 100px; max-height: 100px;" /></a>', image_url))
        output.append(super().render(name, value, attrs, renderer))
        return format_html(''.join(output))


NewsImageFormSet = inlineformset_factory(
    News,
    NewsImage,
    fields=('image',),
    widgets={'image': ImagePreviewWidget},
    extra=1,
    can_delete=True
)


class NewsImagesInline(admin.TabularInline):
    model = NewsImage
    formset = NewsImageFormSet
    extra = 1
    can_delete = True


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImagesInline]
    form = NewsAdminForm


admin.site.register(News, NewsAdmin)
admin.site.register(SliderImage)
