
from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Product, Category, Comment

admin.site.unregister(Group)


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment


def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


make_active.short_description = "Mark selected products as active"


def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


make_inactive.short_description = "Mark selected products as inactive"


def approve_comments(modeladmin, request, queryset):
    queryset.update(is_approved=True)


approve_comments.short_description = "Mark selected products as approved"


def reject_comments(modeladmin, request, queryset):
    queryset.update(is_rejected=False)


reject_comments.short_description = "Mark selected products as rejected"


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProductResource
    list_display = ('name', 'price', 'status_badge', 'updated_at', 'image_tag', 'my_order')
    list_filter = ('updated_at', 'price', 'is_active')
    search_fields = ('name', 'description')
    ordering = ('my_order',)
    actions = [make_active, make_inactive]

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:50px; max-height:50px"/>'.format(obj.image.url))
        return '-'

    image_tag.short_description = 'Image'

    def status_badge(self, obj):
        color = "green" if obj.is_active else "red"
        return format_html('<span style="color:{}; font-weight:bold">{}</span>', color,
                           "Active" if obj.is_active else "Inactive")

    status_badge.short_description = 'Status'


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CategoryResource
    list_display = ('id', 'title',)
    ordering = ('my_order',)
    inlines = [ProductInline]


@admin.register(Comment)
class CommentAdmin(SortableAdminMixin, ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CommentResource
    list_display = ('full_name', 'content', 'status_badge', 'created_at', 'my_order',)
    search_fields = ('text',)
    ordering = ('my_order',)
    list_filter = ('created_at',)
    actions = [approve_comments, reject_comments]

    def status_badge(self, obj):
        color = "green" if obj.is_approved else "red"
        return format_html('<span style="color:{}; font-weight:bold">{}</span>', color,
                           "Approved" if obj.is_approved else "Pending")

    status_badge.short_description = 'Status'
