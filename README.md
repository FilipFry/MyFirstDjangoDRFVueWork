# UV 
* **uv init** - инициализация проекта. (только лишь main.py).<br>
* **uv add django [pillow &#124; ... &#124; djangorestframework &#124; django-filter]** - скачиваем и подключаем в проект пакеты. Например, саму Django, Pillow для пакетов графики.<br>
* **uv run django-admin:**<br>
* **uv run django-admin makemigrations** - Создаём миграции (изменения) для встроенной (а возможно даже внешней) БД.<br>
* **uv run django-admin migrate** - Применяем миграции (изменения) для встроенной (а возможно даже внешней) БД.<br>
* **uv run django-admin startproject** - создаём скелет проекта (аппа) на Django.<br>
Пример:<br>
uv run django-admin startproject MyFirstproject создаст следующие пути:<br>
ПапкаГдеИнициализированПроект \ MyFirstproject (manage.py) \ MyFirstproject (init.py &#124; asgi.py &#124; settings.py &#124; urls.py &#124; wsgi.py)<br>
uv run django-admin startproject MyFirstproject . создаст следующие пути:<br>
ПапкаГдеИнициализированПроект (manage.py) \ MyFirstproject (init.py &#124; asgi.py &#124; settings.py &#124; urls.py &#124; wsgi.py)<br>
* **uv run manage.py runserver** - запсук тестового сервера (только для разработки, не для постоянного использования), который будет доступен по адресу http://127.0.0.1:8000/<br>
# Vue3
(Обязательно надо установить Node.JS)<br>
* **npm create vue@latest** - создание проекта Vue3<br>
+ Features (фишки при установке)
    + Router (SPA development)
    + Pinia (state management)
    + Linter (error prevention)
    + Prettier (code formatting)
* **npm install** - установка и подтягивание необходимых зависимостей в папку проекта VUE<br>
* **npm run dev** - запуск среды разработки / сборщика проекта / так сказать, сервера. Который будет доступен по адресу http://127.0.0.1:5173/<br>
+ Структура каталогов Vue3:
    + main.js - Вход в приложение.
    + index.html - Стандартный html-документ с <div=app> куда как раз и монтируется приложение Vue3.
    + components - тут мы будем складывать и разбивать компоненты
    + assets - статические какие-то данные
    + router - роутинг, маршрутаризация, переходы на страницы, какие компоненты отображать, чем-то похоже на urls.py из gjango, возможно.
    + views - основные базовые компоненты.

# Стрелочные функции JavaScript
function sum (a, b) { return a + b; }<br>
то-же самое, что<br>
const sum = (a, b) => { return a + b; }<br>
<br>
**async** — позволяет использовать await.<br>
**await** — ждет завершения асинхронной операции (например, ответа сервера).<br>
**ref** — хранит изменяемые данные.<br>
**computed** — вычисляет новое значение на основе ref и автоматически обновляется при изменении исходных данных.