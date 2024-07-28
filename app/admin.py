from django.contrib import admin
from shop.models import Category, Product
from import_export.admin import ImportExportModelAdmin


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', "title")
    list_display_links = ('id', "title",)
    search_fields = ('id', 'title', 'slug',)
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'slug', 'description', 'price', 'count',)
    list_display_links = ('id', 'title', 'price', 'count',)
    prepopulated_fields = {'slug': ('title',)}
