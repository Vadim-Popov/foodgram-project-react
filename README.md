# __Foodgram__ 

###### Продуктовый помощник 
___

### Описание проекта

Foodgram это продуктовый помощник, который позволяет пользователям публиковать и искать рецепты.

Каждый рецепт содержит:
- название;
- время приготовления (в минутах);
- список ингредиентов с указанием наименования и дозировки;
- текстовую инструкция приготовления;
- теги, для фильтрации рецептов;
- фото готовых блюд

Пользователи могут добавлять рецепты в избранное, подписываться на авторов и просматривать все их рецепты в разделе "Мои подписки". Также имеется возможность добавлять рецепты в корзину и скачивать файл PDF, содержащий общий список ингредиентов для рецептов в корзине.

Foodgram предоставляет удобный интерфейс для просмотра, создания рецептов и упрощает покупку нужных продуктов.

___

### Технологии

Foodgram использует технологии:

- [Python] (v.3.11) - целевой язык программирования backend
- [Django] (v.4.2.3) - высокоуровневый веб-фреймворк
- [Django REST framework] (v.3.14.0) - инструмент для создания Web API
- [Gunicorn] (v.20.1.0) - Python WSGI HTTP-сервер для UNIX

### Заполняем .env 
- SECRET_KEY = 'секретный ключ из settings'
- DB_NAME = имя базы данных
- POSTGRES_USER = логин для подключения к БД
- POSTGRES_PASSWORD = пароль для подключения к БД
- DB_HOST = название контейнера
- DB_PORT = порт для подключения к БД

### Развертывание проекта на локальном сервере
1. Установите на сервер `docker` и `docker-compose`.
2. Создайте файл `.env`. По примеру как указано выше.
3. Выполните команду `docker-compose up -d --buld`. Из директории `/infra/`
4. Выполните миграции `docker-compose exec backend python manage.py migrate`.
5. Создайте суперюзера `docker-compose exec backend python manage.py createsuperuser`.
6. Соберите статику `docker-compose exec backend python manage.py collectstatic`.
7. `docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/`
8. Заполните базу ингредиентами `docker-compose exec backend python manage.py load_ingredients`.
9. Заполните базу тегами `docker-compose exec backend python manage.py load_tags`.
10. Документация с примерами запросов находится по адресу: <http://localhost/api/docs/redoc.html>.

### Для ревьюера
- Данные от админ панели
Логин: msi@ya.ru
Пароль: msi
Домен: kittygram77.ru

### Автор
[Vadim - Popov](https://github.com/Vadim-Popov)
