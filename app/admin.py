from django.contrib import admin

from app.models import Category, Product, Images, Attribute, AttributeValue, ProductAttribute

from users.models import Customer

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


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'VAT_Number')
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ('created_at',)
    fieldsets = (
        ('basic information:', {
            'fields': ('name', 'email', 'phone', 'VAT_Number', 'slug', 'created_at')
        }),
    )