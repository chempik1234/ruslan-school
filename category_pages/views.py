from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from .models import Category, SidePicture


def category_page(request, category_pk: int):
    category = get_object_or_404(Category, pk=category_pk)
    content_list = []
    content_list.extend(list(category.contents.all()))
    content_list.sort(key=lambda x: x.order)
    return render(request, "category_pages/category.html", context={"content_list": content_list,
                                                                    "title_header": category.title})


def handler404(request, *args, **argv):
    response = render(request, '404.html', {'title_header': 'Ошибка 404'})
    response.status_code = 404
    return response
