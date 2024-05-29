from .models import Category, SidePicture


def default_context(request):
    return {
        'categories': Category.objects.filter(parent_category=None),
        "side_pictures": SidePicture.objects.all()
    }
