from ckeditor.fields import RichTextField
from django.db import models


class Ticket(models.Model):
    closed = models.BooleanField(null=False, blank=False, default=False, verbose_name="Вопрос закрыт")
    email = models.EmailField(null=False, blank=False, max_length=255, verbose_name="Email ответа")
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Тема")
    content = models.TextField(verbose_name="Содержание")
    user = models.ForeignKey('authentication.User', null=True, on_delete=models.SET_NULL,
                             verbose_name="Пользователь")
    date = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        res = self.title + " " + self.email
        if self.closed:
            res = "(закрыто) " + res
        return res

    class Meta:
        verbose_name = "Запрос обратной связи"
        verbose_name_plural = "Запросы обратной связи"
