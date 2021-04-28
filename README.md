# Web application for polls
Application for creating and administering polls

## Requirements
- Docker
- Docker Compose

## For development
1. Clone the repository
2. Rename .env.example to .env and change the variables to yours if needed
```
mv .env.example .env
```
3. Kill postgres processes if needed
```
sudo pkill -u postgres
```
4. Run the docker-compose file dev.yml
```
docker-compose -f docker-compose.dev.yml up -d
```
5. Create a superuser to enter the admin area
```
docker exec -it poll_app_web_1 python manage.py createsuperuser
```
6. If you want you can download my spasde_db database
```
docker exec -it poll_app_web_1 /bin/bash
python manage.py loaddata space_db.json
```
7. Visit localhost:8000

## For production
1. Clone the repository
2. Rename .env.example to .env and and change the variables to yours if needed
```
mv .env.example .env
```
3. Rename .env.example to .env for nginx and change the variables to yours
```
mv nginx/.env.example nginx/.env
```
3. Kill postgres processes if needed
```
sudo pkill -u postgres
```
4. Run the docker-compose file dev.yml
```
docker-compose -f docker-compose.prod.yml up -d
```
5. Create a superuser to enter the admin area
```
docker exec -it poll_app_web_1 python manage.py createsuperuser
```
6. If you want you can download my spasde_db database
```
docker exec -it poll_app_web_1 /bin/bash
python manage.py loaddata space_db.json
```
7. Visit your host address

