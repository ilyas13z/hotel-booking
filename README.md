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
pip install poetry
poetry install
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

---

## Документация
### Сортировка вывода при GET `/rooms/` 
```
/rooms/?ordering={ключ сортировки}
```
### Виды ключей: 
#### По возрастанию:
- `price` - по цене
- `date_added` - по дате добавления
#### По убыванию:
- `-price`
- `-date_added`
