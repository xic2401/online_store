from django.db import models

from apps.users.models import User
from utils.uploads import upload_instance


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Picture(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to=upload_instance)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.id} - image'


class Product(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=255)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена',
                                max_digits=10,
                                decimal_places=2)
    category_id = models.ForeignKey(to=Category,
                                    on_delete=models.SET_NULL,
                                    related_name='product_category',
                                    null=True)
    pictures = models.ManyToManyField(to=Picture,
                                      related_name='product_pictures')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    def __str__(self):
        return self.name

class Rating(models.Model):
    start = models.SmallIntegerField(verbose_name='Количество звёзд')
    product_id = models.ForeignKey(to=Product,
                                   on_delete=models.CASCADE,
                                   related_name='ratings')
    user_id = models.ForeignKey(to=User,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='user_ratings')

    class Meta:
        verbose_name = 'Рейтинг товара'
        verbose_name_plural = 'Рейтинги товара'

    def __str__(self):
        return f'Товар: {self.product.name}, рейтинг: {self.start}'

class Comment(models.Model):
    text = models.TextField(verbose_name='Текст')
    product_id = models.ForeignKey(to=Product,
                                   on_delete=models.CASCADE,
                                   related_name='comments')
    user_id = models.ForeignKey(to=User,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='user_comments')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.text[:100]}...'


