from bookings.models import Booking
from django.test import Client, TestCase
from django.urls import reverse
from rooms.models import Room


class RoomTests(TestCase):
    # Проверяет сортировку списка комнат по цене (по возрастанию)
    def test_rooms_list_returns_rooms_sorted_by_price(self):
        Room.objects.create(description="Room 1", price=100)
        Room.objects.create(description="Room 2", price=50)
        client = Client()
        url = reverse("room-list")
        response = client.get(url + "?ordering=price")
        self.assertEqual(response.status_code, 200)
        prices = [room["price"] for room in response.json()]
        self.assertEqual(prices, sorted(prices))

    # Проверяет сортировку списка комнат по дате добавления
    def test_rooms_list_returns_rooms_sorted_by_date_added(self):
        Room.objects.create(description="Room 1", price=100)
        Room.objects.create(description="Room 2", price=50)
        client = Client()
        url = reverse("room-list")
        response = client.get(url + "?ordering=date_added")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    # Проверяет сортировку списка комнат по цене (по убыванию)
    def test_rooms_list_returns_rooms_sorted_by_price_desc(self):
        Room.objects.create(description="Room 1", price=100)
        Room.objects.create(description="Room 2", price=50)
        client = Client()
        url = reverse("room-list")
        response = client.get(url + "?ordering=-price")
        self.assertEqual(response.status_code, 200)
        prices = [room["price"] for room in response.json()]
        self.assertEqual(prices, sorted(prices, reverse=True))


class BookingTests(TestCase):
    # Проверяет получение списка бронирований для конкретной комнаты
    def test_booking_custom_list_returns_bookings_for_room(self):
        room = Room.objects.create(description="Room 1", price=100)
        Booking.objects.create(
            id_room=room, date_start="2024-07-01", date_end="2024-07-02"
        )
        Booking.objects.create(
            id_room=room, date_start="2024-07-03", date_end="2024-07-04"
        )
        client = Client()
        url = reverse("booking-custom-list")
        response = client.get(url + f"?room_id={room.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    # Проверяет создание нового бронирования через кастомный эндпоинт
    def test_booking_custom_create_creates_booking(self):
        room = Room.objects.create(description="Room 1", price=100)
        client = Client()
        url = reverse("booking-custom-create")
        response = client.post(
            url
            + f"?room_id={room.id}&date_start=2024-07-01&date_end=2024-07-02"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Booking.objects.filter(id_room=room).count(), 1)
        self.assertIn("booking_id", response.json())
