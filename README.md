# Тестовое задание на Python для Firecode

Выполнял: **Иванов Артемий**

## Описание проекта

Система представляет собой REST API и предполагает установку на сервере.

Сервис написан на **Python** с использованием фреймворков **Django**, **Django Rest Framework**

Система реализована на **Python** с использованием фреймворков  
**Django** **Django Rest Framework**, в качестве СУБД используется **PostgreSQL**.

## Развёртывание системы на Linux

1.  Создаём БД:

    `createdb -U postgres firecode`

2.  Копируем локальные настройки в папку с проектом:

    `sh cp .local_settings.py .app./backend/project/local_settings.py`

    Вносим необходимые изменения.

### Развёртывание без использования Docker

1.  Переходим в папку с проекто:

    `sh cd ./app`

2.  Создаём виртуальную среду Python с именем venv:

    `sh python3 -m venv venv`

    и активируем виртуальную среду:

    `sh source ./venv/bin/activate`

3.  Устанавливаем библиотеки Python из файла requirements.txt:

    `sh pip install -r requirements.txt`

4.  Переходим в папку с приложением:

    `sh cd ./backend`

5.  Накатываем миграции БД:
    `sh python manage.py migrate`
6.  Создаём суперпользователя в БД, вводим имя, пароль и email:

    `sh python manage.py createsuperuser`

7.  Запускаем тестовый сервер разработчика:

    `sh python manage.py runserver`

8.  Заполнение базы (не обязательно):
    ```sh
    python manage.py loaddata city/fixtures/city.json
    python manage.py loaddata city/fixtures/street.json
    python manage.py loaddata shop/fixtures/shop.json
    ```

### Развёртывание в Docker

1.  Скопируйте env в папку с докером

    `sh cp env ./docker`

    Отредактируйте содержимое файла env под себя

2.  Переходим в папку с docker:

    `sh cd ./docker`

3.  Собираем образы:
    ```sh
    docker build . -t firecode_web
    cd ./nginx
    docker build . -t firecode_nginx
    cd ../
    ```
4.  Установка зависимостей:
    `sh docker-compose up python_install`
5.  Накатываем миграции БД:
    `sh docker-compose up migrate_db`

6.  Запуск:

    - в dev режиме:
      `sh docker-compose up dev`

    - в production режиме:
      `sh docker-compose up nginx`

7.  Заполнение базы (не обязательно):
    `sh docker-compose up fixtures`

Проект будет доступен по адресу ***http://127.0.0.1:8000/***

## Информация о доступах

## Авторизация

Авторизация необходима только для создания записей.

Авторизация происходит с помощью библиотеки **simplejwt**  
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
