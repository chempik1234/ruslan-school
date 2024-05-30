from cloudinary.models import CloudinaryField
from django import forms

from .models import Content


class ContentAdminForm(forms.ModelForm):
    file = CloudinaryField(
        "Файл",
        overwrite=True,
        resource_type="raw",
    )

    class Meta:
        model = Content
        fields = '__all__'
