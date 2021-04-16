# Web application for polls

Application for creating and administering polls


## For development

1. Clone the repository
2. Rename .env.example to .env and add your variables if necessary
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
6. Visit localhost:8000

## For production

1. Clone the repository
2. Rename .env.example to .env and add your variables if necessary
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
6. Visit localhost:8000

