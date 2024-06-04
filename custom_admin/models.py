from django.db import models
from django.contrib.contenttypes.models import ContentType


class RuslanAdminLog(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.SET_NULL, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    object_id = models.CharField(max_length=50)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField(blank=True)
    action_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Действие администратора'
        verbose_name_plural = 'Действия администратора'

    def __str__(self):
        return f'{self.object_repr} - {self.get_action_flag_display()}'
