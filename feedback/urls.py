from django.urls import path  # , re_path, reverse_lazy
from .views import my_tickets_page, staff_tickets_page, upload_ticket, toggle_ticket

app_name = 'feedback'

urlpatterns = [
    path('my-tickets', my_tickets_page, name='my_tickets'),
    path('feedback', staff_tickets_page, name='feedback_page'),
    path('ticket', upload_ticket, name="upload_feedback"),
    path('toggle/<int:ticket_pk>', toggle_ticket, name="toggle")
]
