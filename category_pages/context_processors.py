from itertools import islice
from .models import Category, SidePicture


def chunks(iterable, n):
    iterator = iter(iterable)
    while True:
        chunk = list(islice(iterator, n))
        if not chunk:
            break
        yield chunk


def default_context(request):
    footer_tabs = [i for i in Category.objects.all() if not i.children.exists()]
    return {
        'categories': Category.objects.filter(parent_category=None),
        "side_pictures": SidePicture.objects.all(),
        "footer_tabs_groups": list(chunks(footer_tabs, 10))
    }
