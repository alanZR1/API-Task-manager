from django.urls import path, include
from rest_framework import routers
from .views import TareaViewSet

router = routers.DefaultRouter()
router.register(r'tareas', TareaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]