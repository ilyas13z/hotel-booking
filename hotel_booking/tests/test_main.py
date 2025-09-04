import pytest
from bookings.models import Booking
from django.urls import reverse
from rooms.models import Room


@pytest.mark.django_db
def test_rooms_list_returns_rooms_sorted_by_price(client):
    # Проверяет сортировку списка комнат по цене (по возрастанию)
    Room.objects.create(description="Room 1", price=100)
    Room.objects.create(description="Room 2", price=50)
    url = reverse("room-list")
    response = client.get(url + "?ordering=price")
    assert response.status_code == 200
    prices = [room["price"] for room in response.json()]
    assert prices == sorted(prices)


@pytest.mark.django_db
def test_rooms_list_returns_rooms_sorted_by_date_added(client):
    # Проверяет сортировку списка комнат по дате добавления
    Room.objects.create(description="Room 1", price=100)
    Room.objects.create(description="Room 2", price=50)
    url = reverse("room-list")
    response = client.get(url + "?ordering=date_added")
    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.django_db
def test_rooms_list_returns_rooms_sorted_by_price_desc(client):
    # Проверяет сортировку списка комнат по цене (по убыванию)
    Room.objects.create(description="Room 1", price=100)
    Room.objects.create(description="Room 2", price=50)
    url = reverse("room-list")
    response = client.get(url + "?ordering=-price")
    assert response.status_code == 200
    prices = [room["price"] for room in response.json()]
    assert prices == sorted(prices, reverse=True)


@pytest.mark.django_db
def test_booking_custom_list_returns_bookings_for_room(client):
    # Проверяет получение списка бронирований для конкретной комнаты
    room = Room.objects.create(description="Room 1", price=100)
    Booking.objects.create(
        id_room=room, date_start="2024-07-01", date_end="2024-07-02"
    )
    Booking.objects.create(
        id_room=room, date_start="2024-07-03", date_end="2024-07-04"
    )
    url = reverse("booking-custom-list")
    response = client.get(url + f"?room_id={room.id}")
    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.django_db
def test_booking_custom_create_creates_booking(client):
    # Проверяет создание нового бронирования через кастомный эндпоинт
    room = Room.objects.create(description="Room 1", price=100)
    url = reverse("booking-custom-create")
    response = client.post(
        url + f"?room_id={room.id}&date_start=2024-07-01&date_end=2024-07-02"
    )
    assert response.status_code == 200
    assert Booking.objects.filter(id_room=room).count() == 1
    assert "booking_id" in response.json()
