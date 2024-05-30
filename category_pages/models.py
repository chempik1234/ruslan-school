from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    parent_category = models.ForeignKey('Category', null=True, blank=True, related_name="children",
                                        verbose_name="Родительская категория", on_delete=models.SET_NULL)
    title = models.CharField(null=False, blank=False, max_length=50, verbose_name="Название", db_index=True,
                             unique=True)

    def __str__(self):
        if self.parent_category:
            return self.title + '<' + str(self.parent_category)
        else:
            return self.title

    class Meta:
        db_table = "ruslan_school_category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


memory_units = ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПТ"]


def convert_file_size(bytes_size):
    unit, size = 0, bytes_size
    while size >= 1024:
        size /= 1024
        unit += 1
    return str(round(size, 1)) + " " + memory_units[unit]


class Content(models.Model):
    parent_category = models.ForeignKey('Category', null=False, blank=False, related_name="contents",
                                        verbose_name="Родительская категория", on_delete=models.CASCADE)
    file = models.FileField(verbose_name="Файл", null=True, blank=True, upload_to="files/",
                            storage=RawMediaCloudinaryStorage())
    text = models.TextField(null=True, blank=True, verbose_name="Текст")
    image = models.ImageField(upload_to="content_images/", null=True, blank=True, verbose_name="Изображение")
    order = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        db_table = "ruslan_school_content"

    def file_size(self):
        if self.file:
            return convert_file_size(self.file.size)
        else:
            return ""

    def __str__(self):
        return "Элемент контента  < " + self.parent_category.title

    class Meta:
        verbose_name = "Элемент контента"
        verbose_name_plural = "Элементы контента"


class SidePicture(models.Model):
    image = models.ImageField(upload_to="side_images/", null=False, blank=False, verbose_name="Изображение")
    link = models.CharField(null=True, blank=True, verbose_name="Ссылка", max_length=300)

    def __str__(self):
        res = "Картинка"
        if self.link:
            return res + " ссылка: " + self.link
        else:
            return res + " без ссылки"

    class Meta:
        verbose_name = "Боковая картинка"
        verbose_name_plural = "Боковые картинки"
