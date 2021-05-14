from django.contrib import admin

from apps.products.models import Category, Product, Rating, Comment, Picture


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category']

    # def get_pictures(self, obj):
    #     if obj.preview:
    #         for pic
    #         return mark_safe(
    #             f'<img src="{obj.preview.url}" alt="" style="width: 100px;" />'
    #         )
    #     return "-"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['start', 'product', 'user']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'product', 'user']
