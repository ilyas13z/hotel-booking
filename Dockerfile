FROM python:3.13-slim AS builder
 
# Create the app directory
RUN mkdir /app
 
# Set the working directory
WORKDIR /app
 
# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
# Upgrade pip and install dependencies
RUN pip install --upgrade pip 

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.13-slim

RUN useradd -m -r appuser && \
   mkdir /app && \
   chown -R appuser /app

COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

WORKDIR /app

COPY --chown=appuser:appuser . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

USER appuser

RUN python /app/hotel_booking/manage.py collectstatic --noinput

EXPOSE 8000 


CMD ["bash", "-c", "python /app/hotel_booking/manage.py makemigrations", "&& python /app/hotel_booking/manage.py migrate && python /app/hotel_booking/manage.py loaddata /app/hotel_booking/rooms/fixtures/rooms.json && python /app/hotel_booking/manage.py loaddata /app/hotel_booking/bookings/fixtures/bookings.json && gunicorn --chdir /app/hotel_booking hotel_booking.wsgi:application --bind 0.0.0.0:8000 --workers 3"]
