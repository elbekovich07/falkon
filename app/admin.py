from django.contrib import admin

from app.models import Category, Product, Images, Attribute, AttributeValue, ProductAttribute

# Register your models here.


# admin.site.register(Category)
admin.site.register(Images)
# admin.site.register(Product)

admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'slug', 'category')
    prepopulated_fields = {"slug": ("name",)}