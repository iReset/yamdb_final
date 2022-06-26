# Проект API YaMDb

<p align="center">

![AutoDeploy](https://github.com/iReset/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

</p>

---

***Проект API YaMDb реализует API для сбора отзывов пользователей на произведения.***

---

## Содержание

- [О проекте](#about)
- [Начало работы](#getting_started)
- [Использование](#usage)
- [Планы](#todo)
- [Использованные средства и технологии](#tools_and_techs)
- [Авторы](#authors)
- [Благодарности](#acknowledgement)

## О проекте<div id="about"></div>

API YaMDb с Docker - это проектная работа шестнадцатого спринта курса "Python-разработчик" Яндекс.Практикум.

Этот проект реализует API будущего сайта, представляющего собой сервис по работе с произведениями и использует Docker для разделения из запуска сервисов.

Произведения делятся на категории:

- Книги,
- Фильмы,
- Музыка.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти. Из пользовательских оценок формируется усреднённая оценка произведения — рейтинг.

Для работы приложения используется docker compose с разделением на три сервера:

- db - с базой данных;
- web - с сайтом;
- nginx - c Nginx.

Для разворачивания проекта на сервере используется GitHub Actions. В процессе
CI производится:

- тестирование;
- сборка Docker-образа и заливка на DockerHub;
- деплой на сервер;
- уведомление в Telegram.

## Начало работы<div id="getting_started"></div>

Для работы с проектом необходимо выполнить действия, описанные ниже.

- Клонировать репозиторий и перейти в него в командной строке:

```sh
git clone git@github.com:iReset/infra_sp2.git
cd infra_sp2/infra
```

При необходимости заполнить поля в .env-файле актуальными данными.

Запустить docker compose:

```sh
docker compose up -d --build
```

Выполнить формирование статики и базы данных:

```sh
docker compose exec web python manage.py collectstatic --no-input
docker compose exec web python manage.py migrate
```

При необходимости заполнить БД тестовыми данными:

```sh
docker compose exec web python manage.py import_data
```

и создать учетную запись администратора:

```sh
docker compose exec web python manage.py createsuperuser
```

## Использование<div id="usage"></div>

Для получения документации по API необходимо открыть в браузере адрес <http://127.0.0.1/redoc/>.

Панель администратора доступна по адресу <http://127.0.0.1/admin/>.

Боевая версия ограниченное время будет доступна по адресам
[ireset.ddns.net](https://ireset.ddns.net/admin) или
[51.250.25.254](http://51.250.25.254/admin).

## Планы<div id="todo"></div>

- Объединить проект API с бекэндом сайта.
- Добавить автозапуск на сервере и перезапуск при падении.
- Добавить тестирование на GitHub при пуше в develop.

## Использованные средства и технологии<div id="tools_and_techs"></div>

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [DRF Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Docker](http://docker.com/)
- [VSCode](https://code.visualstudio.com/)
- [Соглашение о коммитах](https://www.conventionalcommits.org/ru/v1.0.0/)

## Авторы<div id="authors"></div>

- [iReset](https://github.com/iReset) — управление пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения через e-mail, Docker, CI, CD
- [HelloAgni](https://github.com/HelloAgni) — категории (Categories), жанры (Genres) и произведения (Titles): модели, представления и эндпойнты для них
- [Valery-VM](https://github.com/Valery-VM) — отзывы (Review) и комментарии (Comments): описание моделей, представлений, настройка эндпойнтов, определение прав доступа для запросов, рейтинги произведений

## Благодарности<div id="acknowledgement"></div>

- Спасибо команде Яндекс.Практикум за создание курса
- Спасибо наставникам Денису Московченко, Алексею Михайлову и старшему студенту Антону Базуленкову за терпеливые и подробные разъяснения
- Спасибо куратору Екатерине Чапля за неустанную поддержку и организацию работы
- Спасибо команде когорты 28 за поддержку и сопровождение
- Спасибо однокурсникам когорты 28 за дружную команду
