from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rooms.models import Room

from bookings.models import Booking
from bookings.serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(detail=False, methods=["get"], url_path="list")
    def custom_list(self, request, *args, **kwargs):
        id_room = request.query_params.get("room_id")
        bookings = (
            self.get_queryset()
            .filter(id_room_id=id_room)
            .order_by("date_start")
        )
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["post"], url_path="create")
    def custom_create(self, request, *args, **kwargs):
        room_id = request.query_params.get("room_id")
        id_room = Room.objects.get(id=int(room_id))
        date_start = request.query_params.get("date_start")
        date_end = request.query_params.get("date_end")
        booking_element = Booking.objects.create(
            id_room=id_room, date_start=date_start, date_end=date_end
        )
        return Response({"booking_id": booking_element.id})
