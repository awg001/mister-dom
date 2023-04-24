from django.db import models
from django.urls import reverse


# class Slider(models.Model):
#     name = models.CharField(max_length=100)


class Bruschatka(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Характеристики")
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name="Фото")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Цена")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")

    # relation = models.ForeignKey('Slider')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug}': self.slug})

    class Meta:
        verbose_name = 'Тротуарная плитка брусчатка'
        verbose_name_plural = 'Тротуарная плитка брусчатка'
        ordering = ['cat_id', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Виды")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Вид'
        verbose_name_plural = 'Виды'
        ordering = ['id']
