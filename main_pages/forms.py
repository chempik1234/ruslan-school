from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import News


class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = '__all__'
