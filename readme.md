Инструкция для локальной проверки сервиса:
-
```console
docker-compose up
alembic upgrade head
```
Затем заполняем базу тестовыми данными

```console
Swagger доступен по адресу /docs
```

Создать в корне проекта .env файл и добавить содержимое:
```console
POSTGRES_URL=postgresql://user:password@localhost:5432/db
DOTABUFF_LINK=https://ru.dotabuff.com/heroes/
```