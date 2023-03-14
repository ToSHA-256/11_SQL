# 11_SQL

1. Создана БД mbstudents
postgres=# CREATE DATABASE mbstudents;

2. Создан пользователь и пароль.
postgres=# CREATE USER sql_user WITH PASSWORD 'sql_password';

3. Даны привелегии.
postgres=# GRANT ALL PRIVILEGES ON DATABASE dbstudents TO sql_user;

4. Посредствам psycopg2 выполнено подключение к БД
5. Созданы таблицы студентов и аудиторий.
6. Создана таблица взаимосвязей (по принципу многие к многим).
7. Добавлены данные.

