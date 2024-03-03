"""
Это urls.py файл для приложения API.

Он определяет маршруты для доступа к API.

Импортируются следующие классы и функции:

* path и include из django.urls для определения маршрутов;
* DefaultRouter из rest_framework.routers для автоматического создания маршрутов для наборов представлений;
* ProductViewSet, GroupViewSet, LessonViewSet, ProductAccessViewSet из .views для регистрации маршрутов.

Создается экземпляр DefaultRouter и регистрируются наборы просмотров для моделей Product, Group, Lesson, ProductAccess.

Список urlpatterns определяет единый маршрут - включение всех маршрутов, созданных с использованием DefaultRouter.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, GroupViewSet, LessonViewSet, ProductAccessViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'productaccess', ProductAccessViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
