from rest_framework import serializers
from .models import Product, Group, Lesson, ProductAccess

class ProductSerializer(serializers.ModelSerializer):
    students_count = serializers.IntegerField(read_only=True)
    average_group_filling = serializers.FloatField(read_only=True)
    purchase_percent = serializers.SerializerMethodField()
    

    class Meta:
        model = Product
        fields = '__all__'

    def get_purchase_percent(self, obj):
        return obj.get_purchase_percent()

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
        fields = ('id', 'user', 'product', 'group')
