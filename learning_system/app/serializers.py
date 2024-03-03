from rest_framework import serializers
from .models import Product, Group, Lesson, ProductAccess

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'creator', 'name', 'start_date', 'price']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'product', 'name', 'users']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'product', 'name', 'video_link']

class ProductAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAccess
        fields = ['id', 'user', 'product']