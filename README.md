# Сервис авторизации пользователей на FastAPI

## Сервис:

1. ... имеет методы для регистрации (плоть до отправки письма с подтверждением) и авторизации пользователей.
2. ... имеет методы для авторизации и выдачу jwt (access и refresh) токенов.
3. ... имеет методы для обновления jwt (refresh) токенов.
4. ... имеет методы для обновления пароля пользователя (плоть до отправки письма с подтверждением).
5. ... имеет методы для выхода пользователя из системы.

___

## Использовались базы данных:
**SQL**: *PostgresSQL*

*PostgresSQL* -> *SQLAlchemy* -> *asyncpg* -> *Alembic*

**NoSQL**: *Redis*

*Redis* -> *redis*

___

### Перенос проекта на свой репозиторий:
```
git clone https://github.com/daniyarsus/1fit_copy_auth.git
```

### Переход в папку проекта:
```
cd 1fit_copy_auth
cd auth
```

___

### Запуск проекта через uvicorn
```
uvicorn app.main:app --reload
```

___


### API - документация:
```
hhtp://127.0.0.1:8000/docs
```

___

### Запуск проекта через docker
```
docker build -t example .
docker run -d -p 7330:8000 example
http://0.0.0.0:7330 - для доступа к сервису через веб-браузер
http://0.0.0.0:8000 - для доступа к сервису через API
```

___

### Остановка докер контейнера и композа:
```
docker ps -a
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker ps -a
docker-compose down
```

___
### Запуск проекта через docker-compose 
```
docker-compose up
http://0.0.0.0:7330 - для доступа к сервису через веб-браузер
http://0.0.0.0:8000 - для доступа к сервису через API
```

___

### Запуск тестов:
```
pytest tests/auth.py
```

___

### Лицензия:

**NETU**

___

### ToDo:
Сделать код чище