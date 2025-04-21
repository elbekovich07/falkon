from rest_framework import serializers
from .models import Product, Category, Images, ProductAttribute, Attribute, AttributeValue

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'image', 'my_order']

class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = ['id', 'attribute_value']

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['id', 'attribute_key']

class ProductAttributeSerializer(serializers.ModelSerializer):
    attribute_key_id = AttributeSerializer()
    attribute_value_id = AttributeValueSerializer()

    class Meta:
        model = ProductAttribute
        fields = ['attribute_key_id', 'attribute_value_id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'image']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ImageSerializer(many=True)
    product_attributes = ProductAttributeSerializer(many=True)
    discounted_price = serializers.DecimalField(max_digits=14, decimal_places=2, read_only=True)
    get_absolute_url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'price', 'discount', 'discounted_price',
            'quantity', 'category', 'created_at', 'updated_at',
            'images', 'product_attributes', 'get_absolute_url'
        ]
