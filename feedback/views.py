from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import TicketForm
from .models import Ticket


def order_tickets(queryset):
    return queryset.order_by(
        'closed',
        '-date'
    ).all()


@login_required(login_url='authentication:sign_in')
def my_tickets_page(request):
    queryset = order_tickets(Ticket.objects.filter(user=request.user))
    return render(request, "feedback/tickets.html", context={'tickets': queryset,
                                                             "title_header": "Мои запросы",
                                                             "title": "Мои запросы"})


@staff_member_required()
def staff_tickets_page(request):
    queryset = order_tickets(Ticket.objects.all())
    return render(request, "feedback/tickets.html", context={'tickets': queryset,
                                                             "title_header": "Обратная связь",
                                                             "title": "Обратная связь"})


@require_POST
def upload_ticket(request):
    form = TicketForm(request.POST)
    if form.is_valid():
        user = None
        if request.user.is_authenticated:
            user = request.user
        form.save(user=user)
        messages.success(request, "Сохранено!")
        return redirect(request.META.get('HTTP_REFERER', reverse('main_pages:main_page')))
        # redirect('feedback:my_tickets')
    else:
        messages.error(request, "Проверьте ошибки! Не сохранено")
        return redirect(request.META.get('HTTP_REFERER', reverse('main_pages:main_page')))


@require_POST
@login_required(login_url="authentication:sign_in")
def toggle_ticket(request, ticket_pk):
    ticket = get_object_or_404(Ticket, pk=ticket_pk)
    user = ticket.user
    if user == request.user or request.user.is_staff or request.user.is_superuser:
        ticket.closed = not ticket.closed
        ticket.save()
        if ticket.closed:
            messages.success(request, "Вопрос закрыт!")
        else:
            messages.success(request, "Вопрос открыт!")
    else:
        messages.error(request, "У вас недостаточно прав для закрытия вопроса!")
    return redirect(request.META.get('HTTP_REFERER', reverse('main_pages:main_page')))