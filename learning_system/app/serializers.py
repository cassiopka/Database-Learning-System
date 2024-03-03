from rest_framework import serializers
from .models import Product, Group, Lesson, ProductAccess

class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.

    Содержит следующие поля:
    - id: уникальный идентификатор продукта;
    - creator: создатель продукта (связь с моделью User);
    - name: название продукта;
    - start_date: дата начала продукта;
    - students_count: количество студентов, занимающихся на продукте;
    - average_group_filling: среднее значение заполненности групп в процентах;
    - price: цена продукта;
    - purchase_percent: процент приобретения продукта.
    """
    students_count = serializers.IntegerField(read_only=True)
    average_group_filling = serializers.FloatField(read_only=True)
    purchase_percent = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_purchase_percent(self, obj):
        return obj.get_purchase_percent()

class GroupSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Group.

    Содержит следующие поля:
    - id: уникальный идентификатор группы;
    - product: продукт, к которому относится группа (связь с моделью Product);
    - name: название группы;
    - users: список студентов, занимающихся в группе (связь с моделью User через модель ProductAccess).
    """
    class Meta:
        model = Group
        fields = ['id', 'product', 'name', 'users']

class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Lesson.

    Содержит следующие поля:
    - id: уникальный идентификатор урока;
    - product: продукт, к которому относится урок (связь с моделью Product);
    - name: название урока;
    - video_link: ссылка на видео урока.
    """
    class Meta:
        model = Lesson
        fields = ['id', 'product', 'name', 'video_link']

class ProductAccessSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели ProductAccess.

    Содержит следующие поля:
    - id: уникальный идентификатор доступа к продукту;
    - user: студент, получивший доступ к продукту (связь с моделью User);
    - product: продукт, к которому получил доступ студент (связь с моделью Product);
    - group: группа, в которую был распределен студент (связь с моделью Group).
    """
    class Meta:
        model = ProductAccess
        fields = ('id', 'user', 'product', 'group')
