# Database-Learning-System

"Database-Learning-System" - это инновационная платформа, специально созданная для обучения и практики работы с базами данных. Наш проект объединяет в себе широкий спектр функций, направленных на развитие навыков построения связей в базах данных и эффективного написания запросов.

## Технологии:

- Python - в качестве основного языка программирования.
- Django - для создания моделей данных и реализации API.
- SQLite - в качестве базы данных.

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
└── requirements.txt```

## Диаграмма сущностей (Entity Relationship Diagram, ERD).

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
