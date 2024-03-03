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