from rest_framework import viewsets
from .models import Product, Group, Lesson, ProductAccess
from .serializers import ProductSerializer, GroupSerializer, LessonSerializer, ProductAccessSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class ProductAccessViewSet(viewsets.ModelViewSet):
    queryset = ProductAccess.objects.all()
    serializer_class = ProductAccessSerializer