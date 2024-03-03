# Database-Learning-System

"Database-Learning-System" - это инновационная платформа, специально созданная для обучения и практики работы с базами данных. Наш проект объединяет в себе широкий спектр функций, направленных на развитие навыков построения связей в базах данных и эффективного написания запросов.

## Технологии:

- Python - в качестве основного языка программирования.
- Django - для создания моделей данных и реализации API.
- SQLite - в качестве базы данных.



# Диаграмма сущностей (Entity Relationship Diagram, ERD).

Product
-------

* id (primary key)
* creator_id (foreign key to User)
* name
* start_date
* price

Group
-----

* id (primary key)
* product_id (foreign key to Product)
* name

ProductAccess
-------------

* id (primary key)
* user_id (foreign key to User)
* product_id (foreign key to Product)
* group_id (foreign key to Group, null=True, blank=True)

Lesson
------

* id (primary key)
* product_id (foreign key to Product)
* name
* video_link

User
----

* id (primary key)
* username
* password
* email
* first_name
* last_name
* is_staff
* is_active
* date_joined

# API Инструкция

## Базовые сведения

API реализовано с использованием Django REST Framework и предоставляет доступ к следующим моделям:

- Product - продукт
- Group - группа
- Lesson - урок
- ProductAccess - доступ к продукту

## Авторизация

Для доступа к API необходимо авторизоваться с помощью токена. Токен можно получить, авторизовавшись на сайте с использованием логина и пароля.

## Список доступных эндпоинтов

### Продукты

- GET /api/products/ - получить список всех продуктов
- GET /api/products/<pk>/ - получить информацию о конкретном продукте
- POST /api/products/ - создать новый продукт (только для администраторов)
- PUT /api/products/<pk>/ - обновить информацию о продукте (только для администраторов)
- DELETE /api/products/<pk>/ - удалить продукт (только для администраторов)

### Группы

- GET /api/groups/ - получить список всех групп
- GET /api/groups/<pk>/ - получить информацию о конкретной группе
- POST /api/groups/ - создать новую группу (только для администраторов)
- PUT /api/groups/<pk>/ - обновить информацию о группе (только для администраторов)
- DELETE /api/groups/<pk>/ - удалить группу (только для администраторов)

### Уроки

- GET /api/lessons/ - получить список всех уроков
- GET /api/lessons/<pk>/ - получить информацию о конкретном уроке
- POST /api/lessons/ - создать новый урок (только для администраторов)
- PUT /api/lessons/<pk>/ - обновить информацию об уроке (только для администраторов)
- DELETE /api/lessons/<pk>/ - удалить урок (только для администраторов)

### Доступ к продукту

- GET /api/productaccess/ - получить список всех доступов к продуктам
- GET /api/productaccess/<pk>/ - получить информацию о конкретном доступе к продукту
- POST /api/productaccess/ - создать новый доступ к продукту (только для администраторов)
- PUT /api/productaccess/<pk>/ - обновить информацию о доступе к продукту (только для администраторов)
- DELETE /api/productaccess/<pk>/ - удалить доступ к продукту (только для администраторов)




# Структура проекта

```
learning_system/
│
├── core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── tests.py
│
├── .gitignore
├── manage.py
└── requirements.txt
'''
