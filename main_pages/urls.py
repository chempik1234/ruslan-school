from django.urls import path  # , re_path, reverse_lazy
from .views import main_page, news_page, news_details_page

app_name = 'main_pages'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('news', news_page, name='news_page'),
    path('news/<int:news_pk>', news_details_page, name="news_by_id")
]
