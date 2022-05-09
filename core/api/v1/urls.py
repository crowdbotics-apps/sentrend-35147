
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DatesheetViewSet
router = DefaultRouter()
router.register('datesheet', DatesheetViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
