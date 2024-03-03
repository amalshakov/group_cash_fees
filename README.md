# group_cash_fees
Реализован веб-сервис на базе Django, предоставляющий CRUD REST API для групповых денежных сборов.

# Запуск проекта
- Расположить файл .env в одной директории с файлом docker-compose.yml
- Перейти в директорию с файлом docker-compose.yml
- Выполнить команду docker-compose --build
- Из запущенного контейнера, из директории с файлом manage.py выполнить команды:
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py createsuperuser
