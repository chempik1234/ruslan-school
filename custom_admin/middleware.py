from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from custom_admin.models import RuslanAdminLog
from django.contrib.contenttypes.models import ContentType


class CustomAdminLogMiddleware:
    def process_action(self, request, obj, action_flag, change_message=''):
        RuslanAdminLog.objects.create(
            user=request.user,
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.pk,
            object_repr=str(obj),
            action_flag=action_flag,
            change_message=change_message
        )

    def log_addition(self, request, obj, message=''):
        self.process_action(request, obj, ADDITION, message)

    def log_change(self, request, obj, message=''):
        self.process_action(request, obj, CHANGE, message)

    def log_deletion(self, request, obj, message=''):
        self.process_action(request, obj, DELETION, message)
