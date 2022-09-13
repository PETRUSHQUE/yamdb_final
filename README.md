![workflow](https://github.com/petrushque/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
# YamDb Final

Проект YaMDb представлен в виде web-приложения и БД, поднятых в docker контейнерах.\
Собирает отзывы пользователей на произведения. Произведения делятся на категории.
Сами произведения в YaMDb не хранятся. Произведению может быть присвоен жанр из списка предустановленных.
Пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку; 
из пользовательских оценок формируется рейтинг.

## Технологии
- [Yamdb] - Проект Yamdb
- [Django] - Бэкэнд фреймворк
- [Django Rest Framework] - Фрэймворк для создания API на основе Django
- [Django REST Framework Simple JWT] - Библиотека для авторизации с помощью JWT-токенов
- [Django Filter] - Библиотека для фильтрации данных
- [Docker] - ПО для развертывания в контейнере
- [Gunicorn] - WSGI веб-сервер
- [Postgresql] - База данных
- [Nginx] - Веб-сервер

## Установка

### Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:PETRUSHQUE/yamdb_final.git
```
```
cd infra
```
### Наполнить env файл
```
DB_ENGINE=<...> # указываем, что работаем с postgresql
DB_NAME=<...> # имя базы данных
POSTGRES_USER=<...> # логин для подключения к базе данных
POSTGRES_PASSWORD=<...> # пароль для подключения к БД (установите свой)
DB_HOST=<...> # название сервиса (контейнера)
DB_PORT=<...> # порт для подключения к БД
SECRET_KEY=<...>	# ключ для settings.py
```
### Запустить проект:
В первую очередь необходимо собрать контейнеры и запустить их:
```
docker-compose up -d --build
```
Выполнить миграции и собрать статику, поочередно выполнив команды:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input
```
Далее вы можете наполнить БД из файла-фикстуры:
```
docker-compose exec web python manage.py loaddata fixtures.json
```
Внимание: в фикстуре имеется суперпользователь admin;admin,
и если вы хотите создать своего, то воспользуйтесь следующей командой:
```
docker-compose exec web python manage.py createsuperuser
``` 
## Примеры запросов к API и ответов
### Доступно на http://127.0.0.1/redoc/


[//]: # 

   [Yamdb]: <https://github.com/PETRUSHQUE/api_yamdb>
   [Django]: <https://www.djangoproject.com>
   [Django Rest Framework]: <https://www.django-rest-framework.org>
   [Django REST Framework Simple JWT]: <https://github.com/jazzband/djangorestframework-simplejwt>
   [Django Filter]: <https://github.com/carltongibson/django-filter>
   [Docker]: <https://www.docker.com/>
   [Gunicorn]: <https://gunicorn.org/>
   [Postgresql]: <https://www.postgresql.org/>
   [Nginx]: <https://nginx.org/>
