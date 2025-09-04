# Запуск Django проекта

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/ilyas13z/hotel-booking
cd hotel-booking
```

### 2. Создайте и активируйте виртуальное окружение
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установите зависимости
```bash
pip install -r requirements.txt
```

### 4. Скопируйте файл переменных окружения
```bash
cp .env.example .env
```
Отредактируйте `.env` при необходимости.

### 5. Проведите миграции
```bash
python manage.py migrate
```

### 6. Запустите сервер разработки
```bash
python manage.py runserver
```

### 7. Загрузка тестовых данных из фикстур

Для загрузки демонстрационных данных используйте команды:

```bash
python manage.py loaddata rooms/fixtures/rooms.json
python manage.py loaddata bookings/fixtures/bookings.json
```

Это добавит примеры комнат и бронирований в базу данных.

---

## Документация

### Все доступные пути URL

- `/admin/`
  Вход в административную панель Django.

- `/rooms/`
  Получить список всех комнат (`GET`), создать новую комнату (`POST`).  
  [Поддерживает сортировку](#сортировка-вывода-при-get-rooms) через параметр `ordering`.

- `/rooms/{id}/`
  Получить детали комнаты по id (`GET`), обновить (`PUT/PATCH`), удалить (`DELETE`).

- `/bookings/`
  Получить список всех бронирований (`GET`), создать новое бронирование (`POST`).

- `/bookings/{id}/`
  Получить детали бронирования по id (`GET`), обновить (`PUT/PATCH`), удалить (`DELETE`).

- `/bookings/list/`
  Получить список бронирований для конкретной комнаты (`GET`, параметр: `room_id`).

- `/bookings/create/`
  Создать новое бронирование (`POST`, параметры: `room_id`, `date_start`, `date_end`).

---

### Сортировка вывода при GET `/rooms/`
```
/rooms/?ordering={ключ сортировки}
```
#### Виды ключей: 
- По возрастанию: `price`, `date_added`
- По убыванию: `-price`, `-date_added`

---

## Тестирование

Для запуска тестов используйте команду:

```bash
pytest
```

Тесты находятся в директории `src/hotel_booking/tests/`.
