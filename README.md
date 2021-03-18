# Web application for polls

##На русском языке:


1. Клонируем репозиторий
2. Устанавливаем пакет виртуального окружения:
```
pip3 install virtualenv
```
3. Создаем виртуальное окружение для нашего проекта. Переходим в корневую папку проекта и выполняем команду:
```
virtualenv venv
```
4. Активируем виртуальное окружение, находясь в корневой папке проекта:
```
. venv/bin/activate
```
5. Устанавливаем зависимости в ваше виртуальное окружение из файла requirements.txt:
```
pip install -r requirements.txt
```
6. Устанавливаем PostgreSQL:
```
sudo apt install postgresql postgresql-contrib
```
7. Устанавливаем пакеты для работы PostgreSQL с Python:
```
sudo apt-get install libpq-dev python-dev
```
8. Заходим в PostgreSQL:
```
sudo -u postgres psql
```
9. Создаем базу данных для нашего приложения :
```
create database poll_app;
```
10. Создаем роль админа для нашей базы данных с паролем:
```
create role poll_app with login superuser createdb createrole inherit replication connection limit -1 password 'admin';
grant postgres to poll_app;
ALTER DATABASE poll_app OWNER TO poll_app;
```
11. Переименовываем файл .env.example в .env и заполняем соответствующими данными:
```
SECRET_KEY=abc
DEBUG=True
 
DB_NAME=poll_app
DB_USER=poll_app
DB_PASSWORD=admin
DB_HOST=127.0.0.1
DB_PORT=5432
```
12. Создаем таблицы в нашей базе данных:
```
python manage.py migrate
```
13. Запускаем локальный сервер:
```
python manage.py runserver
```

##On english lanquage:


1. Clone the repository
2. Install the virtual environment package:
```
pip3 install virtualenv
```
3. Create a virtual environment. Go to the root folder of the project and execute the command:
```
virtualenv venv
```
4. Activate the virtual environment:
```
. venv/bin/activate
```
5. Install dependencies into your virtual environment from the requirements.txt file:
```
pip install -r requirements.txt
```
6. Install PostgreSQL:
```
sudo apt install postgresql postgresql-contrib
```
7. Install packages for PostgreSQL to work with Python:
```
sudo apt-get install libpq-dev python-dev
```
8. Go to PostgreSQL:
```
sudo -u postgres psql
```
9. Let's create a database for our application:
```
create database poll_app;
```
10. Create an admin role for our database with a password:
```
create role poll_app with login superuser createdb createrole inherit replication connection limit -1 password 'admin';
grant postgres to poll_app;
ALTER DATABASE poll_app OWNER TO poll_app;
```
11. Rename the .env.example file to .env and fill it with the appropriate data:
```
SECRET_KEY=abc
DEBUG=True
 
DB_NAME=poll_app
DB_USER=poll_app
DB_PASSWORD=admin
DB_HOST=127.0.0.1
DB_PORT=5432
```
12. Create tables in database:
```
python manage.py migrate
```
13. Start the local server:
```
python manage.py runserver
```
