from ckeditor.fields import RichTextField
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Заголовок")
    text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Новость " + str(self.created_at) + " " + self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class NewsImage(models.Model):
    news = models.ForeignKey("News", null=False, blank=False, on_delete=models.CASCADE, verbose_name="Новость",
                             related_name="images")
    image = models.ImageField(upload_to="news_images/", null=False, blank=False, verbose_name="Изображение")

    def __str__(self):
        return "Картинка к новости >> (" + str(self.news) + ")"

    class Meta:
        verbose_name = "Картинка к нвости"
        verbose_name_plural = "Картинки к новостям"


class SliderImage(models.Model):
    image = models.ImageField(upload_to="slider_images/", null=False, blank=False, verbose_name="Изображение")
    text = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return 'Картинка на главную <img src="' + self.image.url + '" width="50px"/>'

    class Meta:
        verbose_name = "Картинка на главную"
        verbose_name_plural = "Картинки на главную"
