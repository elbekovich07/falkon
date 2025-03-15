from django.contrib import admin
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Product, Category



class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category



@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProductResource
    list_display = ('name', 'price',  'updated_at', 'image_tag', 'my_order')
    list_filter = ('updated_at', 'price')
    search_fields = ('name', 'description')
    ordering = ('my_order',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:50px; max-height:50px"/>'.format(obj.image.url))
        return '-'

    image_tag.short_description = 'Image'



class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CategoryResource
    list_display = ('id', 'title',)
    ordering = ('my_order',)
    inlines = [ProductInline]