from bookings.views import BookingViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rooms.views import RoomViewSet

router = DefaultRouter()

router.register(r"rooms", RoomViewSet, basename="room")
router.register(r"bookings", BookingViewSet, basename="booking")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
