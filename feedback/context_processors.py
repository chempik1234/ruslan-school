from .forms import TicketForm


def default_context(request):
    return {
        'ticket_form': TicketForm()
    }
