import csv
import json

from django.contrib import admin
from django.http import HttpResponse
from djangoql.admin import DjangoQLSearchMixin

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
class CategoryAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Product)
class ProductAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'slug', 'category')
    prepopulated_fields = {"slug": ("name",)}


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        print(meta.fields)
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = 'Export as CSV'


class ExportJsonMixin:
    def export_as_json(self, request, queryset):
        meta = self.model._meta
        fields_names = [field.name for field in meta.fields]

        data = []
        for obj in queryset:
            row = {}
            for field in fields_names:
                value = getattr(obj, field)
                if hasattr(value, 'isoformat'):
                    value = value.isoformat()

                row[field] = value
            data.append(row)

        response = HttpResponse(
            json.dumps(data, indent=4, default=str),
            content_type='application/json'
        )
        response['Content-Disposition'] = f'attachment; filename={meta}.json'
        return response

    export_as_json.short_description = 'Export as JSON'



@admin.register(Customer)
class CustomerAdmin(ExportCsvMixin, ExportJsonMixin, DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'VAT_Number')
    actions = ['export_as_csv', 'export_as_json']
