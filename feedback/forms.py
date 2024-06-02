from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import Ticket


class TicketForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=100, label="",
                            widget=forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': 'Тема'}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control w-100',
                                                                          'style': 'height: 5em',
                                                                          'placeholder': 'Текст'}),
                              label="")
    email = forms.EmailField(required=True, max_length=255, label="",
                             widget=forms.EmailInput(attrs={'class': 'form-control w-100', 'placeholder': 'Email'}))

    class Meta:
        model = Ticket
        fields = ['title', 'content', 'email']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'})
        #     'content': CKEditorWidget(config_name="basic"),
        # }

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance


