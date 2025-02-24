FROM python:3.12-slim
WORKDIR app/
COPY requirements.txt .
RUN  pip install --upgrade pip
RUN pip install -r requirements.txt
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY . .
EXPOSE 8000
CMD python manage.py makemigrations && python manage.py migrate \
    && python manage.py collectstatic --no-input \
    && gunicorn todo_social_network.wsgi -b 0.0.0.0:8000