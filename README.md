# group_cash_fees
Реализован веб-сервис на базе Django, предоставляющий CRUD REST API для групповых денежных сборов.

# Запуск проекта
- Расположить файл .env в одной директории с файлом docker-compose.yml
- Перейти в директорию с файлом docker-compose.yml
- Выполнить команду docker-compose --build
- Из запущенного контейнера, из директории с файлом manage.py выполнить команды:
  - python manage.py makemigrations
  - python manage.py migrate
- Загрузить manage команды:
  - python manage.py load_user
  - python manage.py load_collect
  - python manage.py load_payment
- Создать суперюзера:
  - python manage.py createsuperuser

# Что бы работала рассылка писем необходимо зайти в файл "signals.py" и полностью его раскомментировать (перед запуском контейнеров). Но, после этого manage-команды работать не будут. SMTP серевер валится из за спама.