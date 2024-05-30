from django.shortcuts import render, get_object_or_404

from .models import News, SliderImage


def main_page(request):
    news = News.objects.all().order_by("-created_at")[: 10]
    latest = news.first()
    return render(request, "main_pages/main_page.html",
                  context={'latest_news': latest, 'news': news,
                           "slider_images": SliderImage.objects.all()})


def news_page(request):
    news = News.objects.all().order_by("-created_at")
    return render(request, "main_pages/news_page.html",
                  context={'news': news, "title_header": "Новости"})


def news_details_page(request, news_pk: int):
    return render(request, "main_pages/post.html", context={"post": get_object_or_404(News, pk=news_pk)})
