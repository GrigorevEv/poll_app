# Web application for polls
Application for creating and administering polls

## Requirements
- Docker
- Docker Compose

## For development
1. Clone the repository
2. Move to poll_app directory
```
cd poll_app
```
3. Rename .env.example to .env and change the variables to yours if needed
```
mv .env.example .env
```
4. Run the docker-compose file dev.yml
```
sudo docker-compose -f docker-compose.dev.yml up -d
```
5. Create a superuser to enter the admin area
```
sudo docker exec -it poll_app_web_1 python manage.py createsuperuser
```
6. If you want you can download my space_db database
```
sudo docker exec -it poll_app_web_1 /bin/bash
python manage.py loaddata space_db.json
```
7. Visit localhost:8000

## For production
1. Clone the repository
2. Move to poll_app directory
```
cd poll_app
```
3. Rename .env.example to .env and and change the variables to yours if needed
```
mv .env.example .env
```
4. Run the docker-compose.prod.yml file
```
sudo docker-compose -f docker-compose.prod.yml up -d
```
5. Create a superuser to enter the admin area
```
sudo docker exec -it poll_app_web_1 python manage.py createsuperuser
```
6. If you want you have to download my space_db database
```
sudo docker exec -it poll_app_web_1 /bin/bash
python manage.py loaddata space_db.json
```
7. Run the Nginx container as shown in the link 
https://github.com/GrigorevEv/Nginx_config_for_two_apps
9. Visit your host address

