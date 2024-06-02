from ckeditor.fields import RichTextField
from django.db import models


class Ticket(models.Model):
    closed = models.BooleanField(null=False, blank=False, default=False)
    email = models.EmailField(null=False, blank=False, max_length=255)
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()
    user = models.ForeignKey('authentication.User', null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now=True)
