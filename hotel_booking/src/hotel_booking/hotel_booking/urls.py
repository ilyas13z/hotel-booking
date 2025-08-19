from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rooms.views import RoomViewSet

router = DefaultRouter()

router.register(r'rooms', RoomViewSet, basename='room')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
